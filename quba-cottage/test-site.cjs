const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--ignore-certificate-errors']
  });
  const context = await browser.newContext({
    ignoreHTTPSErrors: true
  });
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
    // Test main page
    console.log('\n1. Testing main page...');
    await page.goto('https://quba.rent/', {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    const title = await page.title();
    console.log(`   Title: ${title}`);

    // Check hero background image
    const heroImg = await page.$('.hero-bg img');
    console.log(`   Hero image: ${heroImg ? 'Found' : 'NOT FOUND'}`);
    if (heroImg) {
      const src = await heroImg.getAttribute('src');
      console.log(`   Hero src: ${src}`);
    }

    // Check owner image in about section
    console.log('\n2. Checking owner image...');
    const ownerContainer = await page.$('.owner-image-container');
    console.log(`   Owner container: ${ownerContainer ? 'Found' : 'NOT FOUND'}`);

    if (ownerContainer) {
      const ownerImg = await page.$('.owner-image-container img');
      console.log(`   Owner image: ${ownerImg ? 'Found' : 'NOT FOUND'}`);
      if (ownerImg) {
        const src = await ownerImg.getAttribute('src');
        console.log(`   Owner src: ${src}`);
      }
    }

    // Check gallery images
    console.log('\n3. Checking gallery...');
    const galleryImages = await page.$$('.gallery-grid img');
    console.log(`   Gallery images count: ${galleryImages.length}`);

    // Print gallery image sources
    for (let i = 0; i < galleryImages.length; i++) {
      const src = await galleryImages[i].getAttribute('src');
      console.log(`   Gallery image ${i + 1}: ${src}`);
    }

    // Report errors
    console.log('\n=== ERRORS FOUND ===');
    if (errors.length === 0) {
      console.log('No JavaScript errors detected!');
    } else {
      errors.forEach(err => console.log(err));
    }

    console.log('\nTest completed successfully!');

  } catch (err) {
    console.error('Test failed:', err.message);
  } finally {
    await browser.close();
  }
})();
