const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  const errors = [];

  page.on('console', msg => {
    if (msg.type() === 'error' && msg.text().includes('placeholder')) {
      errors.push(msg.text());
    }
  });

  page.on('requestfailed', request => {
    if (request.url().includes('placeholder')) {
      errors.push(`Failed: ${request.url()}`);
    }
  });

  try {
    // Test WITHOUT cache busting
    console.log('=== Test 1: Normal load (may use cached version) ===');
    await page.goto('https://quba.rent/', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });
    await page.waitForTimeout(3000);
    console.log(`Title: ${await page.title()}`);
    
    // Test WITH cache busting
    console.log('\n=== Test 2: With cache-busting parameter ===');
    const page2 = await context.newPage();
    await page2.goto(`https://quba.rent/?v=${Date.now()}`, {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });
    await page2.waitForTimeout(3000);
    console.log(`Title: ${await page2.title()}`);

    // Check HTML content
    const html1 = await page.content();
    const html2 = await page2.content();
    
    const count1 = (html1.match(/via.placeholder.com/g) || []).length;
    const count2 = (html2.match(/via.placeholder.com/g) || []).length;
    
    console.log(`\n=== Results ===`);
    console.log(`Normal load: ${count1} placeholder references`);
    console.log(`Cache-bust load: ${count2} placeholder references`);
    
    if (count2 === 0) {
      console.log('\n✅ SUCCESS: Files on server are correct!');
      console.log('⚠️  Issue: CDN/Proxy is caching old version.');
      console.log('💡 Solution: Clear CDN cache from hosting panel.');
    }

  } catch (error) {
    console.log(`Error: ${error.message}`);
  }

  await browser.close();
})();
