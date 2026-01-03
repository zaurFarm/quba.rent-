#!/usr/bin/env python3
"""
Script to update blog-red-village-ru.html with proper Google Maps satellite view
centered on Krasnaya Sloboda with zoom level 16.
"""

def update_html_with_satellite_view():
    """Update the HTML file with proper Google Maps satellite embed."""
    
    # Read the current file
    with open('/workspace/blog-red-village-ru.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # The new Google Maps satellite/hybrid embed with correct coordinates and zoom
    # Using the data from the user's reference image
    new_satellite_section = '''    <!-- Google Maps Satellite View - Krasnaya Sloboda -->
    <div class="map-section">
      <h2 class="map-title">🛰️ Спутниковая карта Красной Слободы</h2>
      <p class="map-subtitle">Координаты: 41.3635°N, 48.5180°E | Интерактивный спутниковый вид</p>
      
      <div class="interactive-map-container">
        <div class="map-wrapper">
          <div class="google-map-embed">
            <iframe 
              width="100%" 
              height="450" 
              frameborder="0" 
              style="border:0; border-radius: 16px;"
              src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF!5m14!1m13!1m12!1m3!1d3105.5!2d48.518!3d41.3635!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f16!3m3!1m2!1s0x0%3A0x0!2zNDHCsDIxJzU5LjkiTiA0OMKwMzEnMDAuMCJF"
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade"
              title="Красная Слобода - спутниковый вид Google Maps">
            </iframe>
          </div>
        </div>
        
        <div class="info-panel">
          <!-- Default State -->
          <div class="info-default" id="info-default">
            <div class="info-default-icon">🛰️</div>
            <h4>Спутниковая карта Красной Слободы</h4>
            <p>Вы видите реальный спутниковый снимок Красной Слободы (Гырмызы Гасаба) и города Куба</p>
            <p style="margin-top: 15px; color: #2F5233; font-weight: 600;">🏠 «Горный Дом Куба» — ваш уютный дом в сердце Красной Слободы!</p>
          </div>
          
          <!-- Museum Card -->
          <div class="info-card" data-card="museum">
            <div class="info-card-header">
              <div class="info-card-icon">✡️</div>
              <div>
                <div class="info-card-title">Музей горских евреев</div>
                <div class="info-card-distance">📍 800м от «Горного Дома Куба»</div>
              </div>
            </div>
            <p class="info-card-description">Первый музей, посвящённый истории и культуре горских евреев. Расположен в здании исторической синагоги «Карчоги» XIX века. Экспозиция включает традиционные костюмы, ритуальную утварь, старинные рукописи и предметы быта.</p>
            <a href="#booking" class="info-card-action">📌 Забронировать рядом</a>
          </div>
          
          <!-- Synagogue Card -->
          <div class="info-card" data-card="synagogue">
            <div class="info-card-header">
              <div class="info-card-icon">🕍</div>
              <div>
                <div class="info-card-title">Шестикупольная синагога</div>
                <div class="info-card-distance">📍 500м от «Горного Дома Куба»</div>
              </div>
            </div>
            <p class="info-card-description">Архитектурная жемчужина Красной Слободы с шестью куполами. Действующий храм с коллекцией из 70 наставлений для чтения Торы. Прекрасный образец традиционной архитектуры горских евреев.</p>
            <a href="#booking" class="info-card-action">📌 Забронировать рядом</a>
          </div>
          
          <!-- Bridge Card -->
          <div class="info-card" data-card="bridge">
            <div class="info-card-header">
              <div class="info-card-icon">🌉</div>
              <div>
                <div class="info-card-title">Арочный мост Кудиалчай</div>
                <div class="info-card-distance">📍 1.5 км от «Горного Дома Куба»</div>
              </div>
            </div>
            <p class="info-card-description">Исторический кирпичный мост через реку Кудиалчай, построенный в XIX веке. Соединяет Красную Слободу с городом Куба. Живописная прогулка с видом на горы и долину реки.</p>
            <a href="#booking" class="info-card-action">📌 Забронировать рядом</a>
          </div>
          
          <!-- Hotel Card -->
          <div class="info-card" data-card="hotel">
            <div class="info-card-header">
              <div class="info-card-icon">🏠</div>
              <div>
                <div class="info-card-title">Горный Дом Куба</div>
                <div class="info-card-distance">📍 Кушнет Казма, Красная Слобода</div>
              </div>
            </div>
            <p class="info-card-description">Уютный гостевой дом в традиционном стиле с современными удобствами. Идеальная база для исследования Красной Слободы. Тёплая атмосфера, вкусная кухня и гостеприимство хозяев!</p>
            <a href="#booking" class="info-card-action">🛏️ Забронировать номер</a>
          </div>
          
          <!-- River Card -->
          <div class="info-card" data-card="river">
            <div class="info-card-header">
              <div class="info-card-icon">💧</div>
              <div>
                <div class="info-card-title">Река Кудиалчай</div>
                <div class="info-card-distance">📍 Вдоль южной границы Слободы</div>
              </div>
            </div>
            <p class="info-card-description">Живописная река, протекающая между Красной Слободой и городом Куба. Прекрасное место для прогулок, рыбалки и фотосессий. Вода чистая и прохладная даже жарким летом.</p>
            <a href="#booking" class="info-card-action">📌 Забронировать рядом</a>
          </div>
          
          <!-- Quba City Card -->
          <div class="info-card" data-card="quba">
            <div class="info-card-header">
              <div class="info-card-icon">🏘️</div>
              <div>
                <div class="info-card-title">Город Куба</div>
                <div class="info-card-distance">📍 5 км через мост</div>
              </div>
            </div>
            <p class="info-card-description">Районный центр с богатой историей. Знаменит губинскими коврами, мечетями, рынком и живописной набережной. Отличное место для шопинга и знакомства с азербайджанской культурой.</p>
            <a href="#booking" class="info-card-action">📌 Забронировать и посетить</a>
          </div>
          
          <!-- Cemetery Card -->
          <div class="info-card" data-card="cemetery">
            <div class="info-card-header">
              <div class="info-card-icon">✡️</div>
              <div>
                <div class="info-card-title">Еврейское кладбище</div>
                <div class="info-card-distance">📍 Исторический некрополь</div>
              </div>
            </div>
            <p class="info-card-description">Старинное еврейское кладбище с надгробиями, датируемыми несколькими столетиями. Священное место горской еврейской общины. Требует уважительного отношения при посещении.</p>
            <a href="#booking" class="info-card-action">📌 Узнать больше</a>
          </div>
          
          <!-- White Mansion Card -->
          <div class="info-card" data-card="whitemansion">
            <div class="info-card-header">
              <div class="info-card-icon">🏰</div>
              <div>
                <div class="info-card-title">Белый особняк</div>
                <div class="info-card-distance">📍 Знаменитая достопримечательность</div>
              </div>
            </div>
            <p class="info-card-description">Роскошный белый комплекс с красной крышей — один из самых узнаваемых архитектурных памятников Красной Слободы. Величественное здание с большим зелёным садом на берегу реки.</p>
            <a href="#booking" class="info-card-action">📌 Забронировать рядом</a>
          </div>
        </div>
      </div>
    </div>

    <script>
      document.addEventListener('DOMContentLoaded', function() {
        const markers = document.querySelectorAll('.map-marker');
        const infoDefault = document.getElementById('info-default');
        const infoCards = document.querySelectorAll('.info-card');
        
        markers.forEach(marker => {
          marker.addEventListener('click', function() {
            const location = this.getAttribute('data-location');
            
            // Hide all cards and default
            infoDefault.style.display = 'none';
            infoCards.forEach(card => card.classList.remove('active'));
            
            // Show selected card
            const targetCard = document.querySelector(`.info-card[data-card="${location}"]`);
            if (targetCard) {
              targetCard.classList.add('active');
            }
          });
        });
        
        // Close card when clicking outside
        document.addEventListener('click', function(e) {
          if (!e.target.closest('.map-marker') && !e.target.closest('.info-card')) {
            infoDefault.style.display = 'block';
            infoCards.forEach(card => card.classList.remove('active'));
          }
        });
      });
    </script>
'''
    
    # Find and replace the current SVG map section
    import re
    
    # Pattern to match the entire SVG map section
    svg_pattern = r'<!-- Improved SVG Map of Krasnaya Sloboda -->[\s\S]*?</script>\s*'
    
    # Replace with the new satellite embed section
    html_content = re.sub(svg_pattern, new_satellite_section + '\n\n    ', html_content, flags=re.MULTILINE)
    
    # Clean up multiple empty lines
    html_content = re.sub(r'\n{4,}', '\n\n', html_content)
    
    # Write the updated content back
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Successfully updated HTML with proper Google Maps satellite view!")
    print(f"File updated: /workspace/blog-red-village-ru.html")

if __name__ == '__main__':
    update_html_with_satellite_view()
