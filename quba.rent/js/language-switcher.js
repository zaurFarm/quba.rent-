window.switchLanguage = function(lang) {
  var path = window.location.pathname;
  var file = path.split('/').pop() || 'index.html';
  var base = file.replace(/-en\.html|-ru\.html|-ar\.html|\.html/g, '');
  if (base === 'index' || base === '') base = '';
  
  var urls = {
    'az': base ? '/' + base + '.html' : '/',
    'en': base ? '/' + base + '-en.html' : '/en/',
    'ru': base ? '/' + base + '-ru.html' : '/ru/',
    'ar': base ? '/' + base + '-ar.html' : '/ar/'
  };
  
  if (lang === 'blog' || file.indexOf('blog') > -1) {
    urls.az = '/blog.html';
    urls.en = '/blog-en.html';
    urls.ru = '/blog-ru.html';
    urls.ar = '/blog-ar.html';
  }
  
  if (lang === 'tours' || file.indexOf('tours') > -1) {
    urls.az = '/tours.html';
    urls.en = '/tours-en.html';
    urls.ru = '/tours-ru.html';
    urls.ar = '/tours-ar.html';
  }
  
  window.location.href = urls[lang] || '/';
};
