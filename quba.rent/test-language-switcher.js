/**
 * Language Switcher Testing Script
 * Tests language switching functionality across all pages
 */

const { chromium } = require('playwright');

async function testLanguageSwitcher() {
  console.log('🧪 Testing Language Switcher Functionality\n');
  console.log('=' .repeat(60));
  
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  // Collect all errors
  const errors = [];
  
  // Listen for console errors
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push(`Console Error: ${msg.text()}`);
    }
  });
  
  page.on('pageerror', err => {
    errors.push(`Page Error: ${err.message}`);
  });
  
  // Test pages configuration
  const testPages = [
    { url: 'https://quba.rent/', name: 'Main (AZ)', lang: 'az' },
    { url: 'https://quba.rent/en/', name: 'English', lang: 'en' },
    { url: 'https://quba.rent/ar/', name: 'Arabic', lang: 'ar' },
    { url: 'https://quba.rent/ru/', name: 'Russian', lang: 'ru' },
    { url: 'https://quba.rent/blog.html', name: 'Blog (AZ)', lang: 'az' },
    { url: 'https://quba.rent/blog-en.html', name: 'Blog English', lang: 'en' },
    { url: 'https://quba.rent/blog-ar.html', name: 'Blog Arabic', lang: 'ar' },
    { url: 'https://quba.rent/tours.html', name: 'Tours (AZ)', lang: 'az' },
    { url: 'https://quba.rent/tours-en.html', name: 'Tours English', lang: 'en' },
    { url: 'https://quba.rent/tours-ar.html', name: 'Tours Arabic', lang: 'ar' },
    { url: 'https://quba.rent/tours-ru.html', name: 'Tours Russian', lang: 'ru' },
  ];
  
  // Test language switching
  const languageCodes = ['az', 'en', 'ru', 'ar'];
  
  for (const testPage of testPages) {
    console.log(`\n📄 Testing: ${testPage.name}`);
    console.log(`   URL: ${testPage.url}`);
    
    try {
      await page.goto(testPage.url, { waitUntil: 'networkidle', timeout: 30000 });
      console.log(`   ✅ Page loaded successfully`);
      
      // Check if language switcher exists
      const langSwitcher = await page.$('.lang-switch');
      if (langSwitcher) {
        console.log(`   ✅ Language switcher found`);
        
        // Check for language links
        const langLinks = await page.$$('.lang-switch a');
        console.log(`   📊 Found ${langLinks.length} language links`);
        
        // Test clicking each language link
        for (const langCode of languageCodes) {
          try {
            // Find the link for this language
            const link = await page.$(`.lang-switch a[onclick*="switchLanguage('${langCode}')"], .lang-switch a[data-lang="${langCode}"]`);
            
            if (link) {
              // Get the href or onclick attribute
              const href = await link.getAttribute('href');
              const onclick = await link.getAttribute('onclick');
              
              console.log(`   🔄 Language ${langCode.toUpperCase()}: href="${href}", onclick="${onclick}"`);
              
              // Check if href looks correct
              if (href) {
                const expectedSuffixes = {
                  'az': '',
                  'en': '-en',
                  'ru': '-ru',
                  'ar': '-ar'
                };
                
                const isMainPage = testPage.url.endsWith('/') || testPage.url.endsWith('index.html');
                
                if (isMainPage) {
                  // For main pages
                  const expectedUrls = {
                    'az': '/',
                    'en': '/en/',
                    'ru': '/ru/',
                    'ar': '/ar/'
                  };
                  
                  if (href === expectedUrls[langCode] || href.startsWith(expectedUrls[langCode])) {
                    console.log(`      ✅ ${langCode.toUpperCase()} URL correct: ${href}`);
                  } else {
                    console.log(`      ⚠️ ${langCode.toUpperCase()} URL might be incorrect: ${href} (expected: ${expectedUrls[langCode]})`);
                  }
                } else {
                  // For content pages, check if it contains the right suffix
                  if (href.includes(expectedSuffixes[langCode])) {
                    console.log(`      ✅ ${langCode.toUpperCase()} URL contains correct suffix: ${expectedSuffixes[langCode]}`);
                  } else {
                    console.log(`      ⚠️ ${langCode.toUpperCase()} URL missing suffix: ${href} (expected suffix: ${expectedSuffixes[langCode]})`);
                  }
                }
              }
            } else {
              console.log(`   ⚠️ No link found for language ${langCode.toUpperCase()}`);
            }
          } catch (e) {
            console.log(`   ❌ Error testing ${langCode}: ${e.message}`);
          }
        }
      } else {
        console.log(`   ⚠️ No language switcher found`);
      }
      
      // Check for JavaScript errors
      if (errors.length > 0) {
        console.log(`   ❌ JavaScript errors found:`);
        errors.forEach(err => console.log(`      - ${err}`));
        errors.length = 0; // Clear errors for next page
      }
      
    } catch (err) {
      console.log(`   ❌ Failed to load: ${err.message}`);
    }
  }
  
  // Test the actual navigation
  console.log('\n' + '='.repeat(60));
  console.log('🧪 Testing Actual Language Switching\n');
  
  try {
    // Test switching from AZ to EN
    await page.goto('https://quba.rent/', { waitUntil: 'networkidle' });
    const enLink = await page.$('.lang-switch a[onclick*="switchLanguage(\'en\')"]');
    
    if (enLink) {
      const currentUrl = page.url();
      console.log(`📄 Current page: ${currentUrl}`);
      
      // Click the English link
      await enLink.click();
      
      // Wait for navigation
      await page.waitForTimeout(2000);
      
      const newUrl = page.url();
      console.log(`🔄 After clicking EN: ${newUrl}`);
      
      if (newUrl.includes('/en/') || newUrl.endsWith('/en')) {
        console.log(`✅ Successfully navigated to English version`);
      } else {
        console.log(`⚠️ Navigation may have failed. Expected /en/, got: ${newUrl}`);
      }
      
      // Test switching back to AZ
      const azLink = await page.$('.lang-switch a[onclick*="switchLanguage(\'az\')"]');
      if (azLink) {
        await azLink.click();
        await page.waitForTimeout(2000);
        const backUrl = page.url();
        console.log(`🔄 After clicking AZ: ${backUrl}`);
        
        if (backUrl === 'https://quba.rent/' || backUrl.endsWith('/quba.rent/')) {
          console.log(`✅ Successfully navigated back to Azerbaijani version`);
        } else {
          console.log(`⚠️ Navigation back may have failed. Expected /, got: ${backUrl}`);
        }
      }
    } else {
      console.log(`❌ Could not find English language link`);
    }
  } catch (err) {
    console.log(`❌ Error during navigation test: ${err.message}`);
  }
  
  await browser.close();
  
  console.log('\n' + '='.repeat(60));
  console.log('🏁 Testing Complete');
  
  if (errors.length > 0) {
    console.log('\n❌ Errors found during testing:');
    errors.forEach(err => console.log(`   - ${err}`));
    process.exit(1);
  } else {
    console.log('\n✅ No JavaScript errors detected');
    process.exit(0);
  }
}

// Run the test
testLanguageSwitcher().catch(err => {
  console.error('Test failed:', err);
  process.exit(1);
});
