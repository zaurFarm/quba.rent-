const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newContext().then(ctx => ctx.newPage());

  console.log('Testing on /en/ page...\n');
  
  try {
    await page.goto('https://quba.rent/en/', { waitUntil: 'networkidle', timeout: 30000 });
    
    // Check what scripts are on the page
    const scripts = await page.evaluate(() => {
      return Array.from(document.scripts).map(s => ({
        src: s.src,
        innerHTML: s.innerHTML ? s.innerHTML.substring(0, 100) + '...' : '(empty)'
      }));
    });
    
    console.log('Scripts found on page:');
    scripts.forEach((s, i) => {
      console.log(`  ${i+1}. src="${s.src}" - ${s.innerHTML}`);
    });
    
    // Check if switchLanguage exists
    const exists = await page.evaluate(() => typeof window.switchLanguage);
    console.log('\nswitchLanguage exists:', exists);
    
    // Try to call it directly
    if (exists === 'function') {
      console.log('Calling switchLanguage("az")...');
      await page.evaluate(() => window.switchLanguage('az'));
      await page.waitForTimeout(2000);
      console.log('Current URL:', page.url());
    }
    
  } catch (err) {
    console.log('Error:', err.message);
  }
  
  await browser.close();
})();
