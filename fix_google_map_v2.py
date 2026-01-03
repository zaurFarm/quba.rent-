#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fix the Google Maps iframe in blog-red-village-ru.html
Replaces the malformed iframe with a clean one that properly shows
the satellite view of Krasnaya Sloboda at the correct coordinates.
"""

import re
import os

def fix_google_map():
    """
    Find and replace the Google Maps iframe with a properly formatted version
    that shows satellite view of Krasnaya Sloboda.
    """
    
    # File paths
    html_file = '/workspace/blog-red-village-ru.html'
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The new clean iframe with satellite view
    # Using maps.google.com format with t=k for satellite/hybrid view
    new_iframe = '''<iframe 
              width="100%" 
              height="450" 
              frameborder="0" 
              style="border:0; border-radius: 16px;"
              src="https://maps.google.com/maps?q=41.370350,48.514092&z=17&t=k&output=embed"
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              title="Красная Слобода - спутниковый вид Google Maps">
            </iframe>'''
    
    # Method 1: Find the entire google-map-embed div content
    # This pattern matches from the opening div tag to its closing div tag
    map_embed_pattern = r'<div class="google-map-embed">.*?</div>'
    
    # Method 2: If the above fails, find just the iframe
    iframe_pattern = r'<iframe\s+[^>]*google\.com/maps[^>]*></iframe>'
    
    # Try Method 1 first
    match1 = re.search(map_embed_pattern, content, re.DOTALL)
    
    if match1:
        print("✓ Found google-map-embed div")
        old_map_embed = match1.group(0)
        content = content.replace(old_map_embed, f'<div class="google-map-embed">\n            {new_iframe}\n          </div>')
        print("✓ Replaced with clean iframe using Method 1")
    else:
        # Try Method 2
        match2 = re.search(iframe_pattern, content, re.DOTALL)
        
        if match2:
            print("✓ Found Google Maps iframe")
            old_iframe = match2.group(0)
            content = content.replace(old_iframe, new_iframe)
            print("✓ Replaced with clean iframe using Method 2")
        else:
            print("✗ Could not find Google Maps iframe or map embed div")
            print("  Attempting alternative pattern search...")
            
            # Alternative: Look for any iframe containing maps in src
            any_iframe_pattern = r'<iframe[^>]*src="[^"]*maps[^"]*"[^>]*></iframe>'
            match3 = re.search(any_iframe_pattern, content)
            
            if match3:
                print("✓ Found iframe with maps in src")
                old_iframe = match3.group(0)
                content = content.replace(old_iframe, new_iframe)
                print("✓ Replaced with clean iframe using Method 3")
            else:
                print("✗ No map iframe found with any pattern")
                return False
    
    # Write the updated content back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ File updated successfully")
    return True

if __name__ == '__main__':
    print("=" * 60)
    print("Fixing Google Maps iframe for Krasnaya Sloboda")
    print("=" * 60)
    
    success = fix_google_map()
    
    if success:
        print("\n✓ Google Maps iframe has been fixed!")
        print("  - Coordinates: 41.370350, 48.514092")
        print("  - Zoom level: 17")
        print("  - Map type: Satellite (t=k)")
    else:
        print("\n✗ Failed to fix Google Maps iframe")
        exit(1)
