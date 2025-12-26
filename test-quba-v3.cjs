const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  const consoleMessages = [];
  const failedRequests = [];

  // Capture all console messages
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleMessages.push(msg.text());
    }
  });

  // Capture failed requests
  page.on('requestfailed', request => {
    failedRequests.push({
      url: request.url(),
      failure: request.failure().errorText
    });
  });

  try {
    console.log('Navigating to https://quba.rent/...');
    
    await page.goto('https://quba.rent/', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });

    // Wait a bit for JS to execute
    await page.waitForTimeout(5000);

    console.log('Page loaded!');
    console.log(`Title: ${await page.title()}`);

    // Check for placeholder errors specifically
    const placeholderFailures = failedRequests.filter(r => r.url.includes('placeholder'));
    console.log(`\nTotal failed requests: ${failedRequests.length}`);
    console.log(`Placeholder-related failures: ${placeholderFailures.length}`);

    if (placeholderFailures.length > 0) {
      console.log('\nSample of failing URLs:');
      [...new Set(placeholderFailures.map(r => r.url))].slice(0, 10).forEach(url => {
        console.log(`- ${url}`);
      });
    }

    // Check the actual HTML content to verify our edits
    const htmlContent = await page.content();
    const hasPlaceholderInHtml = htmlContent.includes('via.placeholder.com');
    console.log(`\nHTML contains via.placeholder.com: ${hasPlaceholderInHtml}`);

  } catch (error) {
    console.log(`Error: ${error.message}`);
  }

  await browser.close();
})();
