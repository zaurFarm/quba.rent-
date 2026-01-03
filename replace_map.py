#!/usr/bin/env python3
"""
Script to replace the interactive SVG map and satellite map sections 
with a clean Google Maps satellite view iframe.
"""

import re

def replace_maps_with_satellite_view():
    """Read the HTML file, replace map sections, and write back."""
    
    # Read the current file
    with open('/workspace/blog-red-village-ru.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Define the new clean Google Maps satellite iframe
    new_map_section = '''    <!-- Google Maps Satellite View -->
    <div class="satellite-map-section" id="map-location">
      <h2 class="satellite-map-title">🛰️ Спутниковая карта Красной Слободы</h2>
      <p class="satellite-map-subtitle">Исследуйте Красную Слободу с высоты птичьего полёта</p>
      
      <div class="satellite-map-container">
        <iframe 
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2s!4v1735900000000!5m2!1sru!2s!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF"
          width="100%" 
          height="450" 
          style="border:0;" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade"
          title="Красная Слобода - спутниковый вид">
        </iframe>
      </div>
      
      <div class="map-legend">
        <div class="legend-item">
          <div class="legend-dot hotel"></div>
          <span>🏠 «Горный Дом Куба»</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot attraction"></div>
          <span>✡️ Музей и синагоги</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot bridge"></div>
          <span>🌉 Арочный мост</span>
        </div>
      </div>
      
      <div class="location-info">
        <h4>📍 Как нас найти</h4>
        <p>Красная Слобода расположена на левом берегу реки Кудиалчай, в 5 км от города Куба. 
        Наш гостевой дом находится в селении Кушнет Казма, в нескольких минутах ходьбы от главных достопримечательностей.</p>
        <p style="margin-top: 10px;">
          <a href="https://www.google.com/maps/dir//41.3656,48.5118" target="_blank" style="color: #4fc3f7;">
            📍 Открыть маршрут в Google Maps →
          </a>
        </p>
      </div>
    </div>
    '''
    
    # Pattern to match the entire interactive map section (from opening comment to closing script)
    # This matches from "<!-- Interactive Map Section -->" through the closing </script> tag
    interactive_map_pattern = r'<!-- Interactive Map Section -->[\s\S]*?</script>\s*'
    
    # Pattern to match the satellite map section (from opening comment to closing div)
    satellite_map_pattern = r'<!-- Satellite Map Section -->[\s\S]*?</div>\s*'
    
    # Remove both map sections and insert the new one
    # First, remove the interactive map section
    html_content = re.sub(interactive_map_pattern, '', html_content, flags=re.MULTILINE)
    
    # Then, remove the satellite map section
    html_content = re.sub(satellite_map_pattern, new_map_section, html_content, flags=re.MULTILINE)
    
    # Clean up multiple empty lines that might result from the replacement
    html_content = re.sub(r'\n{4,}', '\n\n', html_content)
    
    # Write the updated content back
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Successfully replaced map sections with clean Google Maps satellite view!")
    print(f"File updated: /workspace/blog-red-village-ru.html")

if __name__ == '__main__':
    replace_maps_with_satellite_view()
