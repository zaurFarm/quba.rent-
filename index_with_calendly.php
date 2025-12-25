<?php
$uri = $_SERVER['REQUEST_URI'];
$lang = 'az';

if (preg_match('#^/(az|en|ru|ar)/#', $uri, $matches)) {
    $lang = $matches[1];
}

$files = ['az' => 'index.html', 'en' => 'index-en.html', 'ru' => 'index-ru.html', 'ar' => 'index-ar.html'];

if ($uri == '/' || $uri == '') {
    $file = $files[$lang];
} else {
    $path = ltrim($uri, '/');
    if (preg_match('#\.html$#', $path)) {
        $file = $path;
    } else {
        $file = $files[$lang];
    }
}

$full_path = __DIR__ . '/' . $file;

if (file_exists($full_path)) {
    $html = file_get_contents($full_path);
    $html = str_replace('href="images/', 'href="/images/', $html);
    $html = str_replace('src="images/', 'src="/images/', $html);
    $html = str_replace('href="./', 'href="/', $html);
    
    // Add Calendly widget script to head
    $calendly_head = '<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">';
    $calendly_script = '<script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>';
    
    if (strpos($html, 'assets.calendly.com') === false) {
        $html = str_replace('</head>', $calendly_head . '</head>', $html);
        $html = str_replace('</body>', $calendly_script . '</body>', $html);
    }
    
    echo $html;
} else {
    http_response_code(404);
    echo '<h1>404 Not Found</h1>';
}
?>
