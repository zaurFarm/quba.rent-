/**
 * Quba Cottage - Booking System & SEO Test
 * Tests the booking functionality and SEO optimization
 */

const { chromium } = require('playwright');

async function testWebsite() {
  console.log('🧪 Starting Quba Cottage Website Tests...\n');
  
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  
  const testResults = {
    passed: 0,
    failed: 0,
    tests: []
  };
  
  // Test function
  async function test(name, condition, details = '') {
    try {
      if (condition) {
        testResults.passed++;
        testResults.tests.push({ name, status: '✅ PASS', details });
        console.log(`✅ ${name}`);
      } else {
        testResults.failed++;
        testResults.tests.push({ name, status: '❌ FAIL', details });
        console.log(`❌ ${name} ${details}`);
      }
    } catch (error) {
      testResults.failed++;
      testResults.tests.push({ name, status: '❌ ERROR', details: error.message });
      console.log(`❌ ${name}: ${error.message}`);
    }
  }
  
  try {
    // Load the main page
    console.log('📄 Testing: index.html (Azerbaijani)\n');
    await page.goto(`file://${process.cwd()}/public/index.html`);
    
    // === BOOKING SYSTEM TESTS ===
    console.log('--- Booking System Tests ---');
    
    // Check if booking form exists
    const bookingForm = await page.$('#booking-form');
    await test('Booking form exists', !!bookingForm, 'Form ID: booking-form');
    
    // Check required fields
    const checkin = await page.$('#check-in, #checkin');
    await test('Check-in date field exists', !!checkin, 'Field ID: check-in or checkin');
    
    const checkout = await page.$('#check-out, #checkout');
    await test('Check-out date field exists', !!checkout, 'Field ID: check-out or checkout');
    
    const guests = await page.$('#guests');
    await test('Guests select field exists', !!guests, 'Field ID: guests');
    
    const guestName = await page.$('#guest-name, #guestName');
    await test('Guest name field exists', !!guestName, 'Field ID: guest-name or guestName');
    
    const guestPhone = await page.$('#guest-phone, #guestPhone');
    await test('Guest phone field exists', !!guestPhone, 'Field ID: guest-phone or guestPhone');
    
    const comments = await page.$('#comments, #guest-comments');
    await test('Comments textarea exists', !!comments, 'Field ID: comments');
    
    const submitBtn = await page.$('#submit-booking-btn, button[type="submit"]');
    await test('Submit button exists', !!submitBtn, 'Button for form submission');
    
    // Check WhatsApp integration
    const whatsappScript = await page.$('script[src="js/booking.js"]');
    await test('WhatsApp booking script linked', !!whatsappScript, 'Script: js/booking.js');
    
    // === SEO TESTS ===
    console.log('\n--- SEO Tests ---');
    
    // Check title
    const title = await page.title();
    await test('Title tag exists', !!title, `Title: "${title}"`);
    await test('Title length is optimal (30-60 chars)', title.length >= 30 && title.length <= 60, `Length: ${title.length}`);
    
    // Check meta description
    const description = await page.$eval('meta[name="description"]', el => el.content).catch(() => null);
    await test('Meta description exists', !!description, `Description: "${description?.substring(0, 60)}..."`);
    await test('Description length is optimal (120-160 chars)', description && description.length >= 120 && description.length <= 160, `Length: ${description?.length}`);
    
    // Check keywords
    const keywords = await page.$eval('meta[name="keywords"]', el => el.content).catch(() => null);
    await test('Meta keywords exist', !!keywords, `Keywords: "${keywords}"`);
    
    // Check canonical URL
    const canonical = await page.$eval('link[rel="canonical"]', el => el.href).catch(() => null);
    await test('Canonical URL exists', !!canonical, `URL: "${canonical}"`);
    
    // Check Open Graph
    const ogTitle = await page.$eval('meta[property="og:title"]', el => el.content).catch(() => null);
    await test('Open Graph title exists', !!ogTitle, `OG Title: "${ogTitle}"`);
    
    const ogDescription = await page.$eval('meta[property="og:description"]', el => el.content).catch(() => null);
    await test('Open Graph description exists', !!ogDescription, `OG Description: "${ogDescription?.substring(0, 50)}..."`);
    
    const ogImage = await page.$eval('meta[property="og:image"]', el => el.content).catch(() => null);
    await test('Open Graph image exists', !!ogImage, `OG Image: "${ogImage}"`);
    
    // Check Twitter Cards
    const twitterCard = await page.$eval('meta[name="twitter:card"]', el => el.content).catch(() => null);
    await test('Twitter Card exists', !!twitterCard, `Card: "${twitterCard}"`);
    
    // Check Hreflang
    const hreflangAz = await page.$('link[rel="alternate"][hreflang="az"]');
    await test('Hreflang Azerbaijani exists', !!hreflangAz);
    
    const hreflangEn = await page.$('link[rel="alternate"][hreflang="en"]');
    await test('Hreflang English exists', !!hreflangEn);
    
    const hreflangRu = await page.$('link[rel="alternate"][hreflang="ru"]');
    await test('Hreflang Russian exists', !!hreflangRu);
    
    const hreflangAr = await page.$('link[rel="alternate"][hreflang="ar"]');
    await test('Hreflang Arabic exists', !!hreflangAr);
    
    const hreflangDefault = await page.$('link[rel="alternate"][hreflang="x-default"]');
    await test('Hreflang x-default exists', !!hreflangDefault);
    
    // Check Schema.org
    const schemaOrg = await page.$('script[type="application/ld+json"]');
    await test('Schema.org JSON-LD exists', !!schemaOrg);
    
    if (schemaOrg) {
      const schemaContent = await page.$eval('script[type="application/ld+json"]', el => el.textContent).catch(() => null);
      const isValid = schemaContent && schemaContent.includes('"@type"') && schemaContent.includes('LodgingBusiness');
      await test('Schema.org type is LodgingBusiness', isValid);
      
      const hasName = schemaContent && schemaContent.includes('"name"');
      await test('Schema.org has business name', hasName);
      
      const hasAddress = schemaContent && schemaContent.includes('"address"');
      await test('Schema.org has address', hasAddress);
      
      const hasGeo = schemaContent && schemaContent.includes('"geo"');
      await test('Schema.org has geo coordinates', hasGeo);
      
      const hasAmenity = schemaContent && schemaContent.includes('"amenityFeature"');
      await test('Schema.org has amenities', hasAmenity);
    }
    
    // Check Meta Robots
    const robots = await page.$eval('meta[name="robots"]', el => el.content).catch(() => null);
    await test('Meta robots exists', !!robots, `Content: "${robots}"`);
    await test('Meta robots allows indexing', robots && robots.includes('index'), `Content: "${robots}"`);
    
    // === IMAGE SEO TESTS ===
    console.log('\n--- Image SEO Tests ---');
    
    const images = await page.$$('img');
    await test('Images exist on page', images.length > 0, `Found ${images.length} images`);
    
    let imagesWithAlt = 0;
    for (const img of images) {
      const alt = await img.getAttribute('alt').catch(() => null);
      if (alt) imagesWithAlt++;
    }
    await test('All images have alt attributes', imagesWithAlt === images.length, `${imagesWithAlt}/${images.length} images have alt`);
    
    // === INTERNAL LINKING TESTS ===
    console.log('\n--- Internal Linking Tests ---');
    
    const links = await page.$$('a[href^="#"]');
    await test('Anchor links exist for smooth scroll', links.length > 0, `Found ${links.length} anchor links`);
    
    // === PERFORMANCE TESTS ===
    console.log('\n--- Performance Tests ---');
    
    const hasFavicon = await page.$('link[rel="icon"], link[rel="shortcut icon"]');
    await test('Favicon exists', !!hasFavicon);
    
    const hasViewport = await page.$eval('meta[name="viewport"]', el => el.content).catch(() => null);
    await test('Viewport meta tag exists', !!hasViewport, `Content: "${hasViewport}"`);
    
    const hasCharset = await page.$eval('meta[charset]', el => el.content).catch(() => null);
    await test('Charset meta tag exists', !!hasCharset, `Charset: "${hasCharset}"`);
    
  } catch (error) {
    console.error('Test error:', error.message);
  }
  
  // Print summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 TEST SUMMARY');
  console.log('='.repeat(60));
  console.log(`✅ Passed: ${testResults.passed}`);
  console.log(`❌ Failed: ${testResults.failed}`);
  console.log(`📈 Total: ${testResults.passed + testResults.failed}`);
  console.log('='.repeat(60));
  
  if (testResults.failed === 0) {
    console.log('🎉 All tests passed! Website is ready for deployment.');
  } else {
    console.log('⚠️ Some tests failed. Please review the issues above.');
  }
  
  await browser.close();
  
  // Exit with appropriate code
  process.exit(testResults.failed > 0 ? 1 : 0);
}

// Run tests
testWebsite().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
