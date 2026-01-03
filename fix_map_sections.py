#!/usr/bin/env python3
"""
Script to fix the duplicate map sections and ensure clean Google Maps satellite view.
"""
import re

def fix_map_sections():
    """Read the HTML file, fix duplicate sections, and write back."""
    
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
    
    # Find and remove duplicate map sections
    # First pattern: find the section from "<!-- Google Maps Satellite View -->" to the closing </div> before booking anchor
    duplicate_pattern = r'<!-- Google Maps Satellite View -->[\s\S]*?(?=<div class="map-legend"|<!-- Booking Section Anchor"|<!-- Booking Section Anchor|<div id="booking")'
    
    # Remove all duplicate satellite map sections, keeping only one
    html_content = re.sub(duplicate_pattern, '<!-- Google Maps Satellite View -->', html_content, flags=re.MULTILINE)
    
    # Now clean up and add proper spacing
    html_content = re.sub(r'<!-- Google Maps Satellite View -->\s*', new_map_section + '\n', html_content, count=1, flags=re.MULTILINE)
    
    # Clean up multiple empty lines
    html_content = re.sub(r'\n{4,}', '\n\n', html_content)
    
    # Write the updated content back
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Successfully fixed map sections!")
    print(f"File updated: /workspace/blog-red-village-ru.html")

if __name__ == '__main__':
    fix_map_sections()
