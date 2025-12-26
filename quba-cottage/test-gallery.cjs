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

  console.log('Testing gallery images on https://quba.rent/');
  console.log('='.repeat(60));

  const errors = [];

  // Capture console errors
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push(msg.text());
    }
  });

  page.on('pageerror', err => {
    errors.push(`Page Error: ${err.message}`);
  });

  try {
    // Test main page
    console.log('\n1. Loading main page...');
    await page.goto('https://quba.rent/', {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    console.log('   Title:', await page.title());

    // Check gallery section
    console.log('\n2. Checking gallery section...');
    const gallerySection = await page.$('#gallery');
    console.log('   Gallery section:', gallerySection ? 'Found' : 'NOT FOUND');

    // Get all gallery images
    const galleryImages = await page.$$('.gallery-grid img');
    console.log(`   Gallery images count: ${galleryImages.length}`);

    // Check each image
    console.log('\n3. Checking each gallery image:');
    for (let i = 0; i < galleryImages.length; i++) {
      const img = galleryImages[i];
      const src = await img.getAttribute('src');
      const naturalWidth = await img.evaluate(el => el.naturalWidth);
      const complete = await img.evaluate(el => el.complete);
      const naturalHeight = await img.evaluate(el => el.naturalHeight);

      console.log(`   Image ${i + 1}:`);
      console.log(`      Src: ${src}`);
      console.log(`      Complete (loaded): ${complete}`);
      console.log(`      Dimensions: ${naturalWidth}x${naturalHeight}`);
      console.log(`      Status: ${complete && naturalWidth > 0 ? 'OK ✓' : 'NOT LOADED ✗'}`);
    }

    // Check owner image
    console.log('\n4. Checking owner image...');
    const ownerImg = await page.$('.owner-image-container img');
    if (ownerImg) {
      const src = await ownerImg.getAttribute('src');
      const complete = await ownerImg.evaluate(el => el.complete);
      const naturalWidth = await ownerImg.evaluate(el => el.naturalWidth);
      console.log(`   Owner image src: ${src}`);
      console.log(`   Status: ${complete && naturalWidth > 0 ? 'OK ✓' : 'NOT LOADED ✗'}`);
    } else {
      console.log('   Owner image NOT FOUND');
    }

    // Check hero image
    console.log('\n5. Checking hero image...');
    const heroImg = await page.$('.hero-bg img');
    if (heroImg) {
      const src = await heroImg.getAttribute('src');
      const complete = await heroImg.evaluate(el => el.complete);
      const naturalWidth = await heroImg.evaluate(el => el.naturalWidth);
      console.log(`   Hero image src: ${src}`);
      console.log(`   Status: ${complete && naturalWidth > 0 ? 'OK ✓' : 'NOT LOADED ✗'}`);
    }

    // Report errors
    console.log('\n' + '='.repeat(60));
    console.log('CONSOLE ERRORS:');
    if (errors.length === 0) {
      console.log('   No JavaScript errors detected!');
    } else {
      errors.forEach(err => console.log(`   - ${err}`));
    }

    console.log('\n' + '='.repeat(60));
    console.log('Test completed!');

  } catch (err) {
    console.error('\nTest failed:', err.message);
  } finally {
    await browser.close();
  }
})();
