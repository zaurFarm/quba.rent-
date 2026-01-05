const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const errors = [];
  
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push(`Console Error: ${msg.text()}`);
    }
  });
  
  page.on('pageerror', err => {
    errors.push(`Page Error: ${err.message}`);
  });

  console.log('Testing: https://quba.rent/ar/#contact\n');
  
  try {
    await page.goto('https://quba.rent/ar/#contact', { waitUntil: 'networkidle', timeout: 30000 });
    console.log('Page loaded successfully\n');
    
    // Check if switchLanguage function exists
    const switchLangExists = await page.evaluate(() => typeof window.switchLanguage === 'function');
    console.log('switchLanguage function exists:', switchLangExists);
    
    // Check language switcher buttons
    const langButtons = await page.$$('.lang-switch a');
    console.log('Found language buttons:', langButtons.length);
    
    for (const btn of langButtons) {
      const onclick = await btn.getAttribute('onclick');
      const text = await btn.textContent();
      console.log(`Button "${text}" onclick: ${onclick}`);
    }
    
    // Check for JavaScript errors
    if (errors.length > 0) {
      console.log('\nJavaScript errors:');
      errors.forEach(err => console.log('  -', err));
    } else {
      console.log('\nNo JavaScript errors detected');
    }
    
  } catch (err) {
    console.log('Error loading page:', err.message);
  }
  
  await browser.close();
})();
