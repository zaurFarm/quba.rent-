#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update the Google Maps iframe in blog-red-village-ru.html
with a hybrid satellite view showing the area between Quba and Krasnaya Sloboda.
"""

import re

def update_google_map():
    """
    Update the Google Maps iframe to show hybrid satellite view 
    of the Quba-Krasnaya Sloboda area with proper zoom and markers.
    """
    
    # File paths
    html_file = '/workspace/blog-red-village-ru.html'
    
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # New iframe with hybrid view (satellite + labels)
    # Centered between Quba and Krasnaya Sloboda
    # Zoom level 15 to show the full area and river
    new_iframe = '''<iframe 
              width="100%" 
              height="500" 
              frameborder="0" 
              style="border:0; border-radius: 16px;"
              src="https://maps.google.com/maps?q=41.365,48.515&z=15&t=k&hl=ru&output=embed"
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              title="Красная Слобода - спутниковый вид Google Maps">
            </iframe>'''
    
    # Find the google-map-embed div
    map_embed_pattern = r'<div class="google-map-embed">.*?</div>'
    
    match = re.search(map_embed_pattern, content, re.DOTALL)
    
    if match:
        print("✓ Found google-map-embed div")
        old_map_embed = match.group(0)
        content = content.replace(old_map_embed, f'<div class="google-map-embed">\n            {new_iframe}\n          </div>')
        print("✓ Updated with hybrid satellite view")
        
        # Also update the coordinate text if it exists
        coord_pattern = r'Координаты: 41\.37035015005354°N, 48\.51409202400067°E'
        new_coord_text = 'Координаты: 41.365°N, 48.515°E | Гибридный спутниковый вид'
        
        if re.search(coord_pattern, content):
            content = re.sub(coord_pattern, new_coord_text, content)
            print("✓ Updated coordinate text")
        
        # Write the updated content back
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✓ File updated successfully")
        return True
    else:
        print("✗ Could not find google-map-embed div")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Updating Google Maps to hybrid view")
    print("=" * 60)
    
    success = update_google_map()
    
    if success:
        print("\n✓ Google Maps iframe has been updated!")
        print("  - Center: Between Quba and Krasnaya Sloboda")
        print("  - Coordinates: 41.365, 48.515")
        print("  - Zoom level: 15")
        print("  - Map type: Hybrid satellite (t=k)")
        print("  - Language: Russian (hl=ru)")
    else:
        print("\n✗ Failed to update Google Maps iframe")
        exit(1)
