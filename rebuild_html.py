#!/usr/bin/env python3
"""
Script to rebuild the HTML file with a clean single satellite map section.
"""

def rebuild_html_file():
    """Rebuild the HTML file with correct structure."""
    
    # Read the current file
    with open('/workspace/blog-red-village-ru.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the index of the first satellite map section and the booking section
    first_map_idx = None
    booking_idx = None
    
    for i, line in enumerate(lines):
        if '<!-- Google Maps Satellite View -->' in line:
            if first_map_idx is None:
                first_map_idx = i
        if '<!-- Booking Section Anchor -->' in line:
            booking_idx = i
            break
    
    if first_map_idx is None or booking_idx is None:
        print("Could not find required sections in the file!")
        return
    
    # The new clean satellite map section
    new_map_section = '''            <!-- Google Maps Satellite View -->
    <div class="satellite-map-section" id="map-location">
      <h2 class="satellite-map-title">🛰️ Спутниковая карта Красной Слободы</h2>
      <p class="satellite-map-subtitle">Исследуйте Красную Слободу с высоты птичьего полёта</p>
      
      <div class="satellite-map-container">
        <iframe 
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2s!4v1735900000000!5m2!1sru!2s!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f223!2f70!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF"
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
    
    # Build the new content
    # Keep lines from 0 to first_map_idx-1 (content before map)
    # Add the new clean map section
    # Keep lines from booking_idx to end (booking section and footer)
    
    new_content = ''.join(lines[:first_map_idx])  # Content before map
    new_content += new_map_section  # Clean map section
    new_content += '\n'  # One empty line
    new_content += ''.join(lines[booking_idx:])  # Booking section and footer
    
    # Write the updated content back
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Successfully rebuilt the file with clean map section!")
    print(f"File updated: /workspace/blog-red-village-ru.html")

if __name__ == '__main__':
    rebuild_html_file()
