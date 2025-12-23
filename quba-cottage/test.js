import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Collect console messages
const consoleMessages = [];
page.on('console', msg => {
  consoleMessages.push({ type: msg.type(), text: msg.text() });
});

// Collect page errors
const pageErrors = [];
page.on('pageerror', err => {
  pageErrors.push(err.message);
});

try {
  // Navigate to the HTML file
  await page.goto('file:///workspace/quba-cottage/public/index.html', { waitUntil: 'networkidle' });
  
  // Wait a bit for any dynamic content
  await page.waitForTimeout(2000);
  
  // Check if page loaded successfully
  const title = await page.title();
  console.log('Page title:', title);
  
  // Check for main elements
  const heroExists = await page.$('.hero') !== null;
  const navExists = await page.$('nav') !== null;
  const footerExists = await page.$('footer') !== null;
  
  console.log('Hero section exists:', heroExists);
  console.log('Navigation exists:', navExists);
  console.log('Footer exists:', footerExists);
  
  // Report console messages
  if (consoleMessages.length > 0) {
    console.log('\nConsole messages:');
    consoleMessages.forEach(msg => {
      console.log(`  [${msg.type}] ${msg.text}`);
    });
  } else {
    console.log('\nNo console messages');
  }
  
  // Report page errors
  if (pageErrors.length > 0) {
    console.log('\nPage errors:');
    pageErrors.forEach(err => {
      console.log(`  - ${err}`);
    });
  } else {
    console.log('No page errors');
  }
  
  console.log('\nTest completed successfully!');
  
} catch (error) {
  console.error('Test failed:', error.message);
  process.exit(1);
} finally {
  await browser.close();
}
