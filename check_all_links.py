#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive check of ALL links in all HTML files.
Find any cross-language link issues.
"""

from pathlib import Path
import re

def check_all_links():
    """Check ALL links in HTML files for language consistency."""
    
    html_files = list(Path('/workspace').glob('*.html'))
    
    # Also check subdirectories
    for subdir in Path('/workspace').iterdir():
        if subdir.is_dir() and subdir.name not in ['output', 'user_input_files', 'images', 'node_modules', 'quba-cottage', 'quba-villa-demo']:
            html_files.extend(list(subdir.glob('*.html')))
    
    all_issues = []
    
    for html_file in sorted(set(html_files)):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine expected language from filename
            filename = html_file.name
            
            if '-ru' in filename or filename == 'index-ru.html':
                expected_pages = ['index-ru.html', 'blog-ru.html', 'tours-ru.html']
            elif '-ar' in filename or filename == 'index-ar.html':
                expected_pages = ['index-ar.html', 'blog-ar.html', 'tours-ar.html']
            elif '-en' in filename or filename == 'index-en.html':
                expected_pages = ['index-en.html', 'blog-en.html', 'tours-en.html']
            else:
                continue
            
            # Find all internal links
            link_pattern = r'href="(/[^"]+\.html)"'
            links = re.findall(link_pattern, content)
            
            # Check each link
            for link in links:
                # Skip external links
                if link.startswith('http') or link.startswith('www'):
                    continue
                
                # Check if it's a language-specific page
                for lang in ['-ru', '-ar', '-en']:
                    if lang in link and link not in expected_pages:
                        all_issues.append(f"{filename}: Links to wrong language page: {link}")
                        break
        
        except Exception as e:
            all_issues.append(f"Error processing {html_file.name}: {e}")
    
    return all_issues

if __name__ == '__main__':
    print("=" * 70)
    print("Checking ALL links for cross-language issues")
    print("=" * 70)
    print()
    
    issues = check_all_links()
    
    if issues:
        print(f"Found {len(issues)} issues:\n")
        for issue in issues:
            print(f"  ✗ {issue}")
    else:
        print("✓ No cross-language link issues found!")
    
    print()
    print("=" * 70)
