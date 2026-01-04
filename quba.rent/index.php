<?php
// Redirect to language-specific versions or serve default
$lang = 'az'; // Default to Azerbaijani
$uri = $_SERVER['REQUEST_URI'];

// Handle language prefix - only if explicitly specified in URL
if (preg_match('#^/(az|en|ru|ar)/#', $uri, $matches)) {
    $lang = $matches[1];
}
// If no language prefix and no query parameters, keep default Azerbaijani

// Map language to file
$files = [
    'az' => 'index.html',
    'en' => 'index-en.html',
    'ru' => 'index-ru.html',
    'ar' => 'index-ar.html',
];

$file = isset($files[$lang]) ? $files[$lang] : 'index.html';
$path = __DIR__ . '/' . $file;

// Check if file exists
if (file_exists($path)) {
    // Read and output the HTML file
    $html = file_get_contents($path);
    
    // Update links to use language prefix
    $html = preg_replace('#href="/([^"]*)"#', 'href="/$1"', $html);
    
    // Fix any relative paths
    $html = str_replace('href="images/', 'href="/images/', $html);
    $html = str_replace('src="images/', 'src="/images/', $html);
    
    echo $html;
} else {
    http_response_code(404);
    echo 'File not found: ' . $path;
}
?>






