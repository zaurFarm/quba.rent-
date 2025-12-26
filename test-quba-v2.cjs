const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    bypassCSP: true
  });
  const page = await context.newPage();

  const errors = [];

  // Capture request failures
  page.on('requestfailed', request => {
    const url = request.url();
    if (url.includes('placeholder')) {
      errors.push(`FAILED: ${url}`);
    }
  });

  try {
    console.log('Navigating to https://quba.rent/ with fresh cache...');
    
    const response = await page.goto('https://quba.rent/', {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    console.log(`Status: ${response.status()}`);
    console.log(`Page Title: ${await page.title()}`);
    
    // Wait for any pending requests
    await page.waitForTimeout(2000);

    // Check for any placeholder requests
    const placeholderErrors = errors.filter(e => e.includes('placeholder'));
    console.log(`\nPlaceholder errors found: ${placeholderErrors.length}`);
    
    if (placeholderErrors.length > 0) {
      console.log('\nSample errors:');
      placeholderErrors.slice(0, 5).forEach(e => console.log(e));
    } else {
      console.log('SUCCESS: No placeholder image errors!');
    }

  } catch (error) {
    console.log(`Navigation Error: ${error.message}`);
  }

  await browser.close();
})();
