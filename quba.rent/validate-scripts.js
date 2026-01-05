const fs = require('fs');

// Read the file from FTP (already downloaded)
const html = fs.readFileSync('/tmp/index-ar-ftp.html', 'utf8');

// Extract and validate inline scripts
const scriptRegex = /<script>([\s\S]*?)<\/script>/g;
let match;
let scriptNum = 0;
let errors = [];

while ((match = scriptRegex.exec(html)) !== null) {
  scriptNum++;
  const content = match[1].trim();
  
  // Skip JSON-LD scripts
  if (content.includes('application/ld+json')) continue;
  if (content.length < 10) continue;
  
  try {
    new Function(content);
    console.log('Script ' + scriptNum + ': OK (' + content.length + ' chars)');
  } catch(e) {
    console.log('Script ' + scriptNum + ' ERROR: ' + e.message);
    console.log('Content preview: ' + content.substring(0, 300));
    errors.push(scriptNum);
  }
}

if (errors.length > 0) {
  console.log('\n❌ Found errors in scripts: ' + errors.join(', '));
  process.exit(1);
} else {
  console.log('\n✅ All scripts validated successfully');
}
