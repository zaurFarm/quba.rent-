const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  
  console.log('Testing website: https://quba.rent/');
  
  const errors = [];
  
  // Capture console errors
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push(`Console Error: ${msg.text()}`);
    }
  });
  
  page.on('pageerror', err => {
    errors.push(`Page Error: ${err.message}`);
  });
  
  try {
    // Test main page with domcontentloaded
    console.log('\n1. Testing main page (index.html)...');
    await page.goto('https://quba.rent/', { 
      waitUntil: 'domcontentloaded',
      timeout: 15000 
    });
    
    // Wait a bit for content
    await page.waitForTimeout(3000);
    
    const title = await page.title();
    console.log(`   Title: ${title}`);
    
    // Get page content length to see if it loaded
    const content = await page.content();
    console.log(`   Content length: ${content.length} characters`);
    
    // Check if we have basic HTML structure
    const hasDoctype = content.includes('<!DOCTYPE html>');
    const hasHtmlClose = content.includes('</html>');
    const hasBodyClose = content.includes('</body>');
    
    console.log(`   Has DOCTYPE: ${hasDoctype}`);
    console.log(`   Has </html>: ${hasHtmlClose}`);
    console.log(`   Has </body>: ${hasBodyClose}`);
    
    // Check for key elements
    const heroSection = await page.$('section.hero');
    console.log(`   Hero section: ${heroSection ? 'Found' : 'NOT FOUND'}`);
    
    const navMenu = await page.$('nav');
    console.log(`   Navigation: ${navMenu ? 'Found' : 'NOT FOUND'}`);
    
    // Check for potential issues
    const iframes = await page.$$('iframe');
    console.log(`   Iframes found: ${iframes.length}`);
    
    // Test tours page
    console.log('\n2. Testing tours page...');
    const toursResponse = await page.goto('https://quba.rent/tours.html', { 
      waitUntil: 'networkidle',
      timeout: 30000 
    });
    console.log(`   Status: ${toursResponse.status()}`);
    
    // Report errors
    console.log('\n=== ERRORS FOUND ===');
    if (errors.length === 0) {
      console.log('No JavaScript errors detected!');
    } else {
      errors.forEach(err => console.log(err));
    }
    
  } catch (err) {
    console.error('Test failed:', err.message);
  } finally {
    await browser.close();
  }
})();
