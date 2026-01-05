const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newContext().then(ctx => ctx.newPage());

  const errors = [];
  
  page.on('console', msg => {
    if (msg.type() === 'error') {
      const text = msg.text();
      // Ignore 404 errors for resources
      if (!text.includes('404') && !text.includes('Failed to load resource')) {
        errors.push(`Console: ${text}`);
      }
    }
  });
  
  page.on('pageerror', err => {
    errors.push(`Page: ${err.message}`);
  });

  console.log('Testing: https://quba.rent/ar/\n');
  
  try {
    // Clear cache and load fresh
    await page.goto('https://quba.rent/ar/', { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(2000);
    
    // Check if switchLanguage function exists
    const switchLangExists = await page.evaluate(() => typeof window.switchLanguage === 'function');
    console.log('switchLanguage function exists:', switchLangExists);
    
    // Get the function source if it exists
    if (switchLangExists) {
      const funcSource = await page.evaluate(() => window.switchLanguage.toString());
      console.log('Function source:', funcSource.substring(0, 100) + '...');
    }
    
    // Try clicking the AZ button
    const azBtn = await page.$('.lang-switch a[onclick*="switchLanguage(\'az\')"]');
    if (azBtn) {
      console.log('\nClicking AZ button...');
      await azBtn.click();
      await page.waitForTimeout(3000);
      
      const currentUrl = page.url();
      console.log('Current URL after click:', currentUrl);
      
      if (currentUrl === 'https://quba.rent/' || currentUrl.includes('quba.rent/')) {
        console.log('✅ Language switch to AZ works!');
      } else {
        console.log('❌ Language switch failed. Expected https://quba.rent/, got:', currentUrl);
      }
    } else {
      console.log('❌ AZ button not found');
    }
    
    // Report any syntax errors
    if (errors.length > 0) {
      console.log('\nJavaScript Syntax Errors:');
      errors.forEach(err => console.log('  -', err));
    } else {
      console.log('\n✅ No JavaScript syntax errors detected');
    }
    
  } catch (err) {
    console.log('Error:', err.message);
  }
  
  await browser.close();
})();
