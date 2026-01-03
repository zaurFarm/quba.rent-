#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix all Google Maps iframes with invalid 'pb' parameter.
Replace with clean embed URL for Kusnet Gazma: 41.37035015005354, 48.51409202400067
"""

import os
import re
from pathlib import Path

# Coordinates for Kusnet Gazma
LAT = "41.37035015005354"
LON = "48.51409202400067"
ZOOM = "17"

def fix_google_maps_all():
    """Fix all iframes with pb= parameter using Kusnet Gazma coordinates."""
    
    # Use global coordinates
    html_files = list(Path('/workspace').glob('*.html'))
    
    # Also check subdirectories
    for subdir in Path('/workspace').iterdir():
        if subdir.is_dir() and subdir.name not in ['output', 'user_input_files', 'images', 'node_modules']:
            html_files.extend(list(subdir.glob('*.html')))
    
    fixed_count = 0
    
    for html_file in sorted(set(html_files)):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has pb= in iframe
            if 'maps/embed?pb=' in content:
                # Determine language from file
                lang = 'ru'
                if '-ar' in html_file.name or 'index-ar' in html_file.name:
                    lang = 'ar'
                elif '-en' in html_file.name or 'index-en' in html_file.name:
                    lang = 'en'
                
                # New clean URL
                new_src = f'src="https://maps.google.com/maps?q={LAT},{LON}&z={ZOOM}&t=k&hl={lang}&output=embed"'
                
                # Replace all pb= URLs
                old_pattern = r'src="https://www\.google\.com/maps/embed\?pb=[^"]+"'
                
                if re.search(old_pattern, content):
                    content = re.sub(old_pattern, new_src, content)
                    
                    # Write back
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✓ Fixed: {html_file.name} (lang: {lang})")
                    fixed_count += 1
        
        except Exception as e:
            print(f"✗ Error processing {html_file.name}: {e}")
    
    return fixed_count

if __name__ == '__main__':
    print("=" * 60)
    print("Fixing Google Maps iframes")
    print(f"Coordinates: {LAT}, {LON}")
    print("=" * 60)
    print()
    
    fixed = fix_google_maps_all()
    
    print()
    print("=" * 60)
    print(f"✓ Fixed {fixed} files!")
    print("=" * 60)
