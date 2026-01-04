/**
 * Language Switcher Functionality
 * Handles language switching by dynamically updating URLs
 */

(function() {
  'use strict';

  // Language suffix mappings
  const languageSuffixes = {
    'az': '',
    'en': '-en',
    'ru': '-ru',
    'ar': '-ar'
  };

  // Current page URL
  const currentPath = window.location.pathname;
  
  // Check if we're on a language-specific page
  function getPageInfo() {
    const pathParts = currentPath.split('/').filter(p => p);
    const filename = pathParts[pathParts.length - 1] || 'index.html';
    
    // Detect current language from URL
    let currentLang = 'az';
    if (filename.includes('-en.html') || pathParts.includes('en') && !filename.includes('-')) {
      currentLang = 'en';
    } else if (filename.includes('-ru.html') || pathParts.includes('ru') && !filename.includes('-')) {
      currentLang = 'ru';
    } else if (filename.includes('-ar.html') || pathParts.includes('ar') && !filename.includes('-')) {
      currentLang = 'ar';
    }
    
    // Get page name without language suffix
    let pageName = filename;
    languageSuffixes.forEach((suffix, lang) => {
      if (suffix && filename.endsWith(suffix + '.html')) {
        pageName = filename.replace(suffix + '.html', '.html');
      }
    });
    
    // Special case for index pages
    if (pageName === 'index.html') {
      pageName = '';
    }
    
    return {
      filename: filename,
      currentLang: currentLang,
      pageName: pageName,
      isMainPage: filename === 'index.html' || filename === ''
    };
  }
  
  // Get corresponding page URL for target language
  function getLanguageUrl(targetLang) {
    const info = getPageInfo();
    
    if (info.isMainPage || info.pageName === '') {
      // For main pages, go to main page of target language
      if (targetLang === 'az') {
        return '/';
      } else if (targetLang === 'en') {
        return '/en/';
      } else if (targetLang === 'ru') {
        return '/ru/';
      } else if (targetLang === 'ar') {
        return '/ar/';
      }
    } else {
      // For article/content pages, go to corresponding translated page
      const suffix = languageSuffixes[targetLang];
      // Handle special page names
      let newPageName = info.pageName;
      
      // Special mapping for blog pages
      if (newPageName === 'blog.html') {
        if (targetLang === 'az') return '/blog.html';
        if (targetLang === 'en') return '/blog-en.html';
        if (targetLang === 'ru') return '/blog-ru.html';
        if (targetLang === 'ar') return '/blog-ar.html';
      }
      
      // Special mapping for tours pages
      if (newPageName === 'tours.html') {
        if (targetLang === 'az') return '/tours.html';
        if (targetLang === 'en') return '/tours-en.html';
        if (targetLang === 'ru') return '/tours-ru.html';
        if (targetLang === 'ar') return '/tours-ar.html';
      }
      
      // Standard page mapping
      if (targetLang === 'az') {
        return '/' + newPageName;
      } else {
        return '/' + newPageName.replace('.html', suffix + '.html');
      }
    }
    
    return '/';
  }
  
  // Update all language switcher links
  function updateLanguageLinks() {
    const langLinks = document.querySelectorAll('.lang-switch a[href]');
    
    langLinks.forEach(link => {
      const href = link.getAttribute('href');
      
      // Only process absolute language links
      if (href && href.startsWith('/') && !href.includes('#')) {
        const targetLangMatch = href.match(/\/(az|en|ru|ar)[\/\.]/);
        if (targetLangMatch) {
          const targetLang = targetLangMatch[1];
          const newUrl = getLanguageUrl(targetLang);
          
          if (newUrl !== href) {
            link.setAttribute('href', newUrl);
          }
        }
      }
    });
  }
  
  // Also update inline language switchers in HTML
  function updateInlineLanguageSwitchers() {
    const switchers = document.querySelectorAll('[class*="lang-switch"]');
    
    switchers.forEach(switcher => {
      const links = switcher.querySelectorAll('a');
      links.forEach(link => {
        const text = link.textContent.trim().toLowerCase();
        let targetLang = null;
        
        if (text === 'az' || text.includes('azərbaycan')) targetLang = 'az';
        if (text === 'en' || text.includes('english')) targetLang = 'en';
        if (text === 'ru' || text.includes('русский')) targetLang = 'ru';
        if (text === 'عربي' || text.includes('arabic')) targetLang = 'ar';
        
        if (targetLang) {
          const href = link.getAttribute('href');
          if (href && !href.startsWith('#')) {
            const newUrl = getLanguageUrl(targetLang);
            if (newUrl !== href) {
              link.setAttribute('href', newUrl);
            }
          }
        }
      });
    });
  }
  
  // Initialize when DOM is ready
  function init() {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        updateLanguageLinks();
        updateInlineLanguageSwitchers();
      });
    } else {
      updateLanguageLinks();
      updateInlineLanguageSwitchers();
    }
  }
  
  // Run initialization
  init();
  
  // Expose function globally for manual updates
  window.updateLanguageLinks = updateLanguageLinks;
  
})();
