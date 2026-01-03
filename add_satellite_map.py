#!/usr/bin/env python3
"""
Add satellite Google Map to Red Village article
"""
import re

def add_satellite_map():
    # Read the file
    with open('/workspace/blog-red-village-ru.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if map section already exists
    if 'satellite-map-section' in content:
        print("Satellite map section already exists!")
        return
    
    # CSS styles for satellite map
    satellite_map_css = '''
    /* Satellite Map Styles */
    .satellite-map-section {
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
      padding: 60px 20px;
      margin: 60px 0;
      border-radius: 16px;
      position: relative;
      overflow: hidden;
    }
    .satellite-map-section::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx=\"20\" cy=\"20\" r=\"1\" fill=\"white\" opacity=\"0.1\"/><circle cx=\"80\" cy=\"80\" r=\"1.5\" fill=\"white\" opacity=\"0.1\"/><circle cx=\"50\" cy=\"50\" r=\"1\" fill=\"white\" opacity=\"0.1\"/></svg>');
      pointer-events: none;
    }
    .satellite-map-title {
      text-align: center;
      font-size: 1.8rem;
      color: #4fc3f7;
      margin-bottom: 10px;
      position: relative;
      z-index: 1;
    }
    .satellite-map-subtitle {
      text-align: center;
      color: #90caf9;
      margin-bottom: 30px;
      position: relative;
      z-index: 1;
    }
    .satellite-map-container {
      max-width: 1000px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    }
    .satellite-map-container iframe {
      width: 100%;
      height: 450px;
      border: none;
      display: block;
    }
    .map-legend {
      display: flex;
      justify-content: center;
      gap: 30px;
      margin-top: 25px;
      position: relative;
      z-index: 1;
      flex-wrap: wrap;
    }
    .legend-item {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #e0e0e0;
      font-size: 0.95rem;
    }
    .legend-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }
    .legend-dot.hotel {
      background: #4caf50;
      box-shadow: 0 0 10px #4caf50;
    }
    .legend-dot.attraction {
      background: #f44336;
      box-shadow: 0 0 10px #f44336;
    }
    .legend-dot.bridge {
      background: #ff9800;
      box-shadow: 0 0 10px #ff9800;
    }
    .location-info {
      background: rgba(255,255,255,0.1);
      backdrop-filter: blur(10px);
      padding: 20px 30px;
      border-radius: 12px;
      margin-top: 25px;
      max-width: 1000px;
      margin-left: auto;
      margin-right: auto;
      position: relative;
      z-index: 1;
    }
    .location-info h4 {
      color: #4fc3f7;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .location-info p {
      color: #e0e0e0;
      margin: 0;
    }
    .location-info a {
      color: #4fc3f7;
      text-decoration: none;
    }
    @media (max-width: 600px) {
      .satellite-map-container iframe {
        height: 350px;
      }
      .map-legend {
        gap: 15px;
      }
    }
    '''
    
    # Insert CSS before closing style tag
    content = content.replace('  </style>', satellite_map_css + '\n  </style>')
    
    # HTML for satellite map section
    satellite_map_html = '''
    <!-- Satellite Map Section -->
    <div class="satellite-map-section">
      <h2 class="satellite-map-title">🛰️ Спутниковая карта Красной Слободы</h2>
      <p class="satellite-map-subtitle">Координаты: 41.3656°N, 48.5118°E | Гырмызы Гасаба, Азербайджан</p>
      
      <div class="satellite-map-container">
        <iframe 
          src="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d310.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!4v1735900000000!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.5118!3d41.3656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2sus!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzAnNDguNCJF"
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade"
          title="Красная Слобода на спутниковой карте">
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
    
    # Insert before CTA section
    content = content.replace(
        '<div class="cta-section">',
        satellite_map_html + '\n\n    <div class="cta-section">'
    )
    
    # Write the updated content
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Satellite map added to article!")
    print(f"  File: /workspace/blog-red-village-ru.html")
    print(f"  Coordinates: 41.3656°N, 48.5118°E")

if __name__ == "__main__":
    add_satellite_map()
