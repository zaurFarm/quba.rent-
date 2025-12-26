const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  const consoleMessages = [];
  const errors = [];

  // Capture console messages
  page.on('console', msg => {
    const text = msg.text();
    consoleMessages.push(`[${msg.type()}] ${text}`);
    if (msg.type() === 'error') {
      errors.push(text);
    }
  });

  // Capture page errors
  page.on('pageerror', error => {
    errors.push(`Page Error: ${error.message}`);
  });

  // Capture request failures
  page.on('requestfailed', request => {
    errors.push(`Failed Request: ${request.url()} - ${request.failure().errorText}`);
  });

  try {
    console.log('Navigating to https://quba.rent/...');
    
    // Navigate with timeout
    const response = await page.goto('https://quba.rent/', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });

    console.log(`Status: ${response.status()}`);
    
    // Wait a bit for JS to execute
    await page.waitForTimeout(3000);

    // Check if main elements exist
    const title = await page.title();
    console.log(`Page Title: ${title}`);

    // Check for key elements
    const hasHeader = await page.$('header') !== null;
    const hasBody = await page.$('body') !== null;
    const bodyContent = await page.evaluate(() => document.body.innerHTML.length);
    
    console.log(`Has header: ${hasHeader}`);
    console.log(`Has body: ${hasBody}`);
    console.log(`Body content length: ${bodyContent} characters`);

    if (errors.length > 0) {
      console.log('\n=== ERRORS FOUND ===');
      errors.forEach((err, i) => console.log(`${i + 1}. ${err}`));
    } else {
      console.log('\nNo errors detected!');
    }

    if (consoleMessages.length > 0) {
      console.log('\n=== Console Messages ===');
      consoleMessages.forEach(msg => console.log(msg));
    }

  } catch (error) {
    console.log(`Navigation Error: ${error.message}`);
  }

  await browser.close();
})();
