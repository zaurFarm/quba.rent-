#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check all HTML files for navigation link issues.
Ensure all links stay within the same language.
"""

from pathlib import Path
import re

def check_navigation_links():
    """Check navigation links in all HTML files."""
    
    html_files = list(Path('/workspace').glob('*.html'))
    
    # Also check subdirectories
    for subdir in Path('/workspace').iterdir():
        if subdir.is_dir() and subdir.name not in ['output', 'user_input_files', 'images', 'node_modules', 'quba-cottage', 'quba-villa-demo']:
            html_files.extend(list(subdir.glob('*.html')))
    
    issues = []
    
    for html_file in sorted(set(html_files)):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine expected language from filename
            filename = html_file.name
            
            if '-ru' in filename or filename == 'index-ru.html':
                expected_lang = 'ru'
                expected_home = '/index-ru.html'
                expected_tours = '/tours-ru.html'
                expected_blog = '/blog-ru.html'
            elif '-ar' in filename or filename == 'index-ar.html':
                expected_lang = 'ar'
                expected_home = '/index-ar.html'
                expected_tours = '/tours-ar.html'
                expected_blog = '/blog-ar.html'
            elif '-en' in filename or filename == 'index-en.html':
                expected_lang = 'en'
                expected_home = '/index-en.html'
                expected_tours = '/tours-en.html'
                expected_blog = '/blog-en.html'
            else:
                continue  # Skip files without language indicator
            
            # Find navigation section
            nav_pattern = r'<ul class="nav-links">(.*?)</ul>'
            nav_match = re.search(nav_pattern, content, re.DOTALL)
            
            if nav_match:
                nav_content = nav_match.group(0)
                
                # Check for cross-language links in navigation
                if '/index-' in nav_content and expected_home not in nav_content:
                    # Find wrong language links
                    wrong_links = re.findall(r'href="(/index-[^"]+\.html)"', nav_content)
                    for link in wrong_links:
                        if link != expected_home:
                            issues.append(f"{filename}: Wrong home link: {link} (expected: {expected_home})")
                
                if '/tours-' in nav_content and expected_tours not in nav_content:
                    wrong_links = re.findall(r'href="(/tours-[^"]+\.html)"', nav_content)
                    for link in wrong_links:
                        if link != expected_tours:
                            issues.append(f"{filename}: Wrong tours link: {link} (expected: {expected_tours})")
                
                if '/blog-' in nav_content and expected_blog not in nav_content:
                    wrong_links = re.findall(r'href="(/blog-[^"]+\.html)"', nav_content)
                    for link in wrong_links:
                        if link != expected_blog:
                            issues.append(f"{filename}: Wrong blog link: {link} (expected: {expected_blog})")
        
        except Exception as e:
            issues.append(f"Error processing {html_file.name}: {e}")
    
    return issues

if __name__ == '__main__':
    print("=" * 70)
    print("Checking navigation links for language consistency")
    print("=" * 70)
    print()
    
    issues = check_navigation_links()
    
    if issues:
        print(f"Found {len(issues)} issues:\n")
        for issue in issues:
            print(f"  ✗ {issue}")
    else:
        print("✓ All navigation links are language-consistent!")
    
    print()
    print("=" * 70)
