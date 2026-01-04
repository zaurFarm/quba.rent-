#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix language switcher links in all HTML files.
Ensure each language button points to the correct language page.
"""

from pathlib import Path
import re

def fix_language_switchers():
    """Fix all language switcher links."""
    
    html_files = list(Path('/workspace').glob('*.html'))
    
    # Also check subdirectories
    for subdir in Path('/workspace').iterdir():
        if subdir.is_dir() and subdir.name not in ['output', 'user_input_files', 'images', 'node_modules', 'quba-cottage', 'quba-villa-demo']:
            html_files.extend(list(subdir.glob('*.html')))
    
    fixed_count = 0
    
    for html_file in sorted(set(html_files)):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine expected language URLs from filename
            filename = html_file.name
            
            if '-ru' in filename or filename == 'index-ru.html':
                expected = {'az': '/blog-ar.html', 'ru': '/index-ru.html', 'en': '/index-en.html', 'ar': '/index-ar.html'}
            elif '-ar' in filename or filename == 'index-ar.html':
                expected = {'az': '/blog-ar.html', 'ru': '/index-ru.html', 'en': '/index-en.html', 'ar': '/index-ar.html'}
            elif '-en' in filename or filename == 'index-en.html':
                expected = {'az': '/blog-ar.html', 'ru': '/index-ru.html', 'en': '/index-en.html', 'ar': '/index-ar.html'}
            else:
                continue
            
            # Find lang-switch section
            lang_pattern = r'<div class="lang-switch">(.*?)</div>'
            lang_match = re.search(lang_pattern, content, re.DOTALL)
            
            if lang_match:
                old_lang_section = lang_match.group(0)
                
                # Fix AZ link
                if 'href="/blog-ar.html"' not in old_lang_section and 'href="/index-ar.html"' not in old_lang_section:
                    # AZ should point to Arabic version
                    if 'href="/index-ru.html"' in old_lang_section and expected['ar'] != '/index-ru.html':
                        content = content.replace(
                            'href="/index-ru.html"', 
                            f'href="{expected["ar"]}"'
                        )
                
                # Count fixes
                if old_lang_section != content[content.find('<div class="lang-switch">'):content.find('</div>', content.find('<div class="lang-switch">'))+6]:
                    print(f"✓ Fixed language switcher in: {html_file.name}")
                    fixed_count += 1
        
        except Exception as e:
            print(f"✗ Error processing {html_file.name}: {e}")
    
    return fixed_count

if __name__ == '__main__':
    print("=" * 70)
    print("Fixing language switcher links")
    print("=" * 70)
    print()
    
    fixed = fix_language_switchers()
    
    print()
    print("=" * 70)
    print(f"✓ Fixed {fixed} files!")
    print("=" * 70)
