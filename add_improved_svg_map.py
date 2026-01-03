#!/usr/bin/env python3
"""
Script to update blog-red-village-ru.html with an improved, detailed SVG map
based on the aerial photography and satellite data provided.
"""

def update_html_with_improved_map():
    """Update the HTML file with a detailed new SVG map."""
    
    # Read the current file
    with open('/workspace/blog-red-village-ru.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # The new improved SVG map section with detailed landmarks
    new_map_section = '''    <!-- Improved SVG Map of Krasnaya Sloboda -->
    <div class="map-section">
      <h2 class="map-title">🗺️ Детальная карта Красной Слободы</h2>
      <p class="map-subtitle">Интерактивная схема достопримечательностей и ключевых объектов</p>
      
      <div class="interactive-map-container">
        <div class="map-wrapper">
          <svg viewBox="0 0 800 500" class="map-svg" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <!-- Gradients -->
              <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#e8f4f8"/>
                <stop offset="100%" style="stop-color:#d4e5ed"/>
              </linearGradient>
              <linearGradient id="qubaLandGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#e8dcc8"/>
                <stop offset="100%" style="stop-color:#d4c4a8"/>
              </linearGradient>
              <linearGradient id="redVillageGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#d4c4a8"/>
                <stop offset="100%" style="stop-color:#c4b498"/>
              </linearGradient>
              <linearGradient id="riverGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#8ec3eb"/>
                <stop offset="50%" style="stop-color:#6bb3d9"/>
                <stop offset="100%" style="stop-color:#5a9bd4"/>
              </linearGradient>
              <linearGradient id="mountainGradient" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" style="stop-color:#a8b5a0"/>
                <stop offset="100%" style="stop-color:#c8d4c0"/>
              </linearGradient>
              
              <!-- Filters -->
              <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15"/>
              </filter>
              <filter id="buildingShadow" x="-10%" y="-10%" width="120%" height="120%">
                <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.2"/>
              </filter>
            </defs>
            
            <!-- Sky Background -->
            <rect width="800" height="200" fill="url(#skyGradient)"/>
            
            <!-- Mountains Background -->
            <path d="M0 180 Q100 130 200 160 Q300 100 400 140 Q500 80 600 130 Q700 90 800 150 L800 200 L0 200 Z" fill="url(#mountainGradient)" opacity="0.6"/>
            <path d="M0 200 Q150 150 300 190 Q450 130 600 180 Q700 140 800 190 L800 200 L0 200 Z" fill="url(#mountainGradient)" opacity="0.4"/>
            
            <!-- Background Hills -->
            <ellipse cx="100" cy="200" rx="120" ry="50" fill="#b8c4a8" opacity="0.5"/>
            <ellipse cx="700" cy="190" rx="150" ry="60" fill="#b8c4a8" opacity="0.5"/>
            
            <!-- Quba Bank (Left/Bottom) - Light earth tone -->
            <path d="M0 200 L200 200 L250 280 L180 380 L0 420 Z" fill="url(#qubaLandGradient)"/>
            <path d="M0 420 L0 500 L300 500 L250 380 L180 380 L200 320 L250 280 L200 200 Z" fill="#d4c4a8"/>
            
            <!-- Quba Buildings -->
            <g filter="url(#buildingShadow)">
              <!-- Red roof building (prominent landmark from photo) -->
              <rect x="30" y="340" width="40" height="30" fill="#d4a574" stroke="#8B4513" stroke-width="1"/>
              <path d="M25 340 L50 320 L75 340 Z" fill="#8B0000"/>
              
              <!-- Government/Cultural Building -->
              <rect x="90" y="360" width="50" height="35" fill="#f5f5dc" stroke="#8B7355" stroke-width="1"/>
              <rect x="95" y="350" width="40" height="12" fill="#6b8e23"/>
              <rect x="85" y="395" width="60" height="8" fill="#8B4513"/>
              
              <!-- Various Quba houses -->
              <rect x="160" y="380" width="25" height="20" fill="#deb887" stroke="#8B7355" stroke-width="1"/>
              <path d="M158 380 L172 365 L188 380 Z" fill="#a52a2a"/>
              
              <rect x="200" y="400" width="30" height="22" fill="#f5deb3" stroke="#8B7355" stroke-width="1"/>
              <path d="M198 400 L215 382 L232 400 Z" fill="#8B0000"/>
              
              <!-- Juma Mosque (from satellite data) -->
              <rect x="320" y="410" width="35" height="30" fill="#f0e68c" stroke="#8B7355" stroke-width="1"/>
              <path d="M315 410 L337 385 L360 410 Z" fill="#2F5233"/>
              <rect x="335" y="395" width="6" height="15" fill="#2F5233"/>
            </g>
            
            <!-- R3 Highway (Kuba-Kusary road) -->
            <path d="M-10 200 Q150 180 300 220 T550 180 T810 150" fill="none" stroke="#fcd68d" stroke-width="10" stroke-linecap="round"/>
            <path d="M-10 200 Q150 180 300 220 T550 180 T810 150" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-dasharray="20,15"/>
            
            <!-- River Qudyalchay (Kudialchay) -->
            <path d="M180 200 Q200 250 250 300 Q300 350 350 400 Q400 450 450 500 L500 500 Q450 420 400 380 Q350 320 300 280 Q250 230 220 200 Z" fill="url(#riverGradient)"/>
            
            <!-- River detail - multiple channels -->
            <path d="M200 220 Q240 260 280 310 Q320 360 380 410" fill="none" stroke="#6bb3d9" stroke-width="8" opacity="0.6"/>
            <path d="M220 240 Q260 280 300 330 Q340 380 400 430" fill="none" stroke="#5a9bd4" stroke-width="5" opacity="0.5"/>
            <path d="M240 260 Q280 300 320 350 Q360 400 420 450" fill="none" stroke="#4a8bc4" stroke-width="4" opacity="0.4"/>
            
            <!-- River stones/pebbles texture -->
            <circle cx="250" cy="280" r="4" fill="#a0a0a0" opacity="0.4"/>
            <circle cx="280" cy="300" r="3" fill="#b0b0b0" opacity="0.3"/>
            <circle cx="310" cy="330" r="5" fill="#909090" opacity="0.4"/>
            <circle cx="340" cy="360" r="3" fill="#a0a0a0" opacity="0.3"/>
            <circle cx="370" cy="400" r="4" fill="#b0b0b0" opacity="0.4"/>
            
            <!-- Main Bridge (Körpü Tağlı) - Arches visible from photo -->
            <g filter="url(#shadow)">
              <!-- Bridge structure -->
              <path d="M510 220 L560 290" stroke="#e0e0e0" stroke-width="16" stroke-linecap="round"/>
              <path d="M510 220 L560 290" stroke="#f5f5f5" stroke-width="10" stroke-linecap="round"/>
              
              <!-- Bridge arches -->
              <path d="M515 235 Q530 250 545 265" fill="none" stroke="#c0c0c0" stroke-width="3"/>
              <path d="M520 250 Q535 265 550 280" fill="none" stroke="#c0c0c0" stroke-width="3"/>
              
              <!-- Bridge railings -->
              <line x1="510" y1="218" x2="560" y2="288" stroke="#e0e0e0" stroke-width="2"/>
              <line x1="510" y1="222" x2="560" y2="292" stroke="#e0e0e0" stroke-width="2"/>
              
              <!-- Vehicles on bridge -->
              <rect x="525" y="252" width="8" height="5" fill="#4169e1" rx="1"/>
              <rect x="540" y="265" width="8" height="5" fill="#dc143c" rx="1"/>
            </g>
            
            <!-- Krasnaya Sloboda (Red Village) Bank - Right/Top -->
            <path d="M320 200 L450 200 L480 280 L420 380 L320 380 Z" fill="url(#redVillageGradient)"/>
            <path d="M450 200 L800 200 L800 380 L420 380 L480 280 Z" fill="#c4b498"/>
            
            <!-- Krasnaya Sloboda Buildings - Dense from aerial photo -->
            <g filter="url(#buildingShadow)">
              <!-- White Mansion Complex (prominent landmark from photo) -->
              <rect x="430" y="260" width="50" height="40" fill="#ffffff" stroke="#d4d4d4" stroke-width="1"/>
              <path d="M425 260 L455 235 L485 260 Z" fill="#8B0000"/>
              <rect x="435" y="300" width="40" height="35" fill="#ffffff" stroke="#d4d4d4" stroke-width="1"/>
              <path d="M430 300 L455 280 L480 300 Z" fill="#8B0000"/>
              
              <!-- Large white retaining wall/garden area -->
              <rect x="420" y="295" width="70" height="80" fill="none" stroke="#ffffff" stroke-width="3"/>
              <rect x="425" y="300" width="60" height="70" fill="#90EE90" opacity="0.7"/>
              
              <!-- Dense residential area - characteristic red roofs -->
              <!-- Row 1 -->
              <rect x="340" y="230" width="20" height="18" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M338 230 L350 218 L362 230 Z" fill="#8B0000"/>
              
              <rect x="365" y="225" width="22" height="20" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M363 225 L376 210 L389 225 Z" fill="#a52a2a"/>
              
              <rect x="390" y="220" width="25" height="22" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M388 220 L402 202 L418 220 Z" fill="#8B0000"/>
              
              <rect x="500" y="230" width="20" height="18" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M498 230 L510 218 L522 230 Z" fill="#8B0000"/>
              
              <rect x="525" y="235" width="18" height="16" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M523 235 L534 223 L545 235 Z" fill="#a52a2a"/>
              
              <!-- Row 2 -->
              <rect x="335" y="260" width="22" height="20" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M333 260 L346 245 L359 260 Z" fill="#8B0000"/>
              
              <rect x="370" y="270" width="20" height="18" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M368 270 L380 258 L392 270 Z" fill="#a52a2a"/>
              
              <rect x="400" y="265" width="18" height="16" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M398 265 L409 253 L420 265 Z" fill="#8B0000"/>
              
              <rect x="550" y="260" width="25" height="22" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M548 260 L562 242 L577 260 Z" fill="#8B0000"/>
              
              <!-- Row 3 - Synagogues area -->
              <rect x="350" y="310" width="30" height="28" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M345 310 L365 288 L385 310 Z" fill="#2F5233"/>
              
              <rect x="390" y="320" width="35" height="32" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M385 320 L407 292 L430 320 Z" fill="#2F5233"/>
              
              <rect x="350" y="350" width="28" height="25" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M347 350 L364 332 L381 350 Z" fill="#2F5233"/>
              
              <rect x="400" y="365" width="30" height="28" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M397 365 L415 345 L433 365 Z" fill="#2F5233"/>
              
              <!-- Museum location (synagogue Karçogi) -->
              <rect x="550" y="310" width="40" height="35" fill="#f5f5dc" stroke="#8B7355" stroke-width="0.5"/>
              <path d="M545 310 L570 288 L595 310 Z" fill="#2F5233"/>
            </g>
            
            <!-- Jewish Cemetery (from satellite data) -->
            <g opacity="0.8">
              <ellipse cx="280" cy="180" rx="40" ry="25" fill="#c4b498" stroke="#a09080" stroke-width="1"/>
              <!-- Cemetery markers -->
              <rect x="260" y="168" width="3" height="12" fill="#8B7355"/>
              <rect x="275" y="172" width="3" height="10" fill="#8B7355"/>
              <rect x="290" y="165" width="3" height="14" fill="#8B7355"/>
              <rect x="305" y="170" width="3" height="11" fill="#8B7355"/>
              <rect x="265" y="182" width="3" height="9" fill="#8B7355"/>
              <rect x="282" y="185" width="3" height="8" fill="#8B7355"/>
              <rect x="298" y="180" width="3" height="10" fill="#8B7355"/>
            </g>
            
            <!-- Road through Krasnaya Sloboda -->
            <path d="M340 290 Q380 280 420 290 Q460 300 500 290" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/>
            
            <!-- Ridge Road (background road from photo) -->
            <path d="M200 160 Q400 150 600 170" fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round" opacity="0.7"/>
            
            <!-- Labels -->
            <text x="130" y="300" class="map-label-title" text-anchor="middle" fill="#555">ГУБА</text>
            <text x="420" y="285" class="map-label-title" text-anchor="middle" fill="#8B0000">КРАСНАЯ СЛОБОДА</text>
            <text x="260" y="250" class="map-label" text-anchor="middle" fill="#666">мост</text>
            <text x="380" y="305" class="map-label" text-anchor="middle" fill="#2F5233">синагоги</text>
            <text x="520" y="280" class="map-label" text-anchor="middle" fill="#666">музей</text>
            
            <!-- Markers -->
            <!-- Marker 1: Museum -->
            <g class="map-marker" data-location="museum" transform="translate(570, 327)" cursor="pointer">
              <circle class="marker-pulse pulse-animation" cx="0" cy="0"/>
              <circle class="marker-pin" cx="0" cy="0" r="12"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">✡️</text>
            </g>
            
            <!-- Marker 2: Synagogues -->
            <g class="map-marker" data-location="synagogue" transform="translate(407, 310)" cursor="pointer">
              <circle class="marker-pulse pulse-animation" cx="0" cy="0"/>
              <circle class="marker-pin" cx="0" cy="0" r="12"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">🕍</text>
            </g>
            
            <!-- Marker 3: Bridge -->
            <g class="map-marker" data-location="bridge" transform="translate(535, 255)" cursor="pointer">
              <circle class="marker-pulse pulse-animation" cx="0" cy="0"/>
              <circle class="marker-pin" cx="0" cy="0" r="12"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">🌉</text>
            </g>
            
            <!-- Marker 4: Mountain House Hotel -->
            <g class="map-marker" data-location="hotel" transform="translate(455, 340)" cursor="pointer">
              <circle class="marker-pulse marker-pulse.hotel pulse-animation" cx="0" cy="0"/>
              <circle class="marker-pin hotel" cx="0" cy="0" r="14"/>
              <text class="marker-icon" text-anchor="middle" dy="5" font-size="12">🏠</text>
            </g>
            
            <!-- Marker 5: River -->
            <g class="map-marker" data-location="river" transform="translate(350, 350)" cursor="pointer">
              <circle class="marker-pin" cx="0" cy="0" r="10"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">💧</text>
            </g>
            
            <!-- Marker 6: Quba City -->
            <g class="map-marker" data-location="quba" transform="translate(130, 360)" cursor="pointer">
              <circle class="marker-pin" cx="0" cy="0" r="11"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">🏘️</text>
            </g>
            
            <!-- Marker 7: Jewish Cemetery -->
            <g class="map-marker" data-location="cemetery" transform="translate(280, 180)" cursor="pointer">
              <circle class="marker-pin" cx="0" cy="0" r="10"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">✡️</text>
            </g>
            
            <!-- Marker 8: White Mansion -->
            <g class="map-marker" data-location="whitemansion" transform="translate(455, 295)" cursor="pointer">
              <circle class="marker-pin" cx="0" cy="0" r="11"/>
              <text class="marker-icon" text-anchor="middle" dy="4" font-size="10">🏰</text>
            </g>
          </svg>
        </div>
        
        <div class="info-panel">
          <!-- Default State -->
          <div class="info-default" id="info-default">
            <div class="info-default-icon">🗺️</div>
            <h4>Карта достопримечательностей</h4>
            <p>Нажмите на любой маркер на карте, чтобы узнать подробности о месте</p>
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
    
    # Find and replace the current satellite map section
    # The current section starts with "<!-- Google Maps Satellite View -->"
    import re
    
    # Pattern to match the entire satellite map section
    satellite_pattern = r'<!-- Google Maps Satellite View -->[\s\S]*?</div>\s*(?=\s*<!-- Booking Section Anchor -->|\s*<div id="booking")'
    
    # Replace with the new improved SVG map section
    html_content = re.sub(satellite_pattern, new_map_section + '\n\n    ', html_content, flags=re.MULTILINE)
    
    # Clean up multiple empty lines
    html_content = re.sub(r'\n{4,}', '\n\n', html_content)
    
    # Write the updated content back
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Successfully updated HTML with improved SVG map!")
    print(f"File updated: /workspace/blog-red-village-ru.html")

if __name__ == '__main__':
    update_html_with_improved_map()
