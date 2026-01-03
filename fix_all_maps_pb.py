#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix all Google Maps iframes with invalid 'pb' parameter.
Replace with clean embed URL.
"""

import os
from pathlib import Path

def fix_google_maps_pb():
    """Fix all iframes with pb= parameter."""
    
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
                # Extract coordinates from the old URL
                import re
                
                # Pattern to match the old iframe src with pb parameter
                pattern = r'src="https://www\.google\.com/maps/embed\?pb=([^"]+)"'
                
                matches = re.findall(pattern, content)
                
                if matches:
                    # Find the coordinates
                    coord_pattern = r'!3d([\d.]+)!2d([\d.]+)'
                    coord_match = re.search(coord_pattern, matches[0])
                    
                    if coord_match:
                        lat = coord_match.group(1)
                        lon = coord_match.group(2)
                        
                        # Determine language from file or URL
                        lang = 'ru'
                        if '-ar' in html_file.name:
                            lang = 'ar'
                        elif '-en' in html_file.name:
                            lang = 'en'
                        
                        # New clean URL
                        new_src = f'src="https://maps.google.com/maps?q={lat},{lon}&z=15&t=k&hl={lang}&output=embed"'
                        old_src = f'src="https://www.google.com/maps/embed?pb={matches[0]}"'
                        
                        content = content.replace(old_src, new_src)
                        
                        # Write back
                        with open(html_file, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        print(f"✓ Fixed: {html_file.name} ({lat}, {lon})")
                        fixed_count += 1
                    else:
                        print(f"⚠ Could not extract coords from: {html_file.name}")
                else:
                    print(f"⚠ No matches found in: {html_file.name}")
        
        except Exception as e:
            print(f"✗ Error processing {html_file.name}: {e}")
    
    return fixed_count

if __name__ == '__main__':
    print("=" * 60)
    print("Fixing Google Maps iframes (removing 'pb' parameter)")
    print("=" * 60)
    print()
    
    fixed = fix_google_maps_pb()
    
    print()
    print("=" * 60)
    print(f"✓ Fixed {fixed} files!")
    print("=" * 60)
