from ftplib import FTP
import os

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

# Coordinates
LAT = "41.275389"
LON = "48.337667"

# New working Google Maps embed URL (without problematic pb parameter)
# Using the directions embed format which always works
MAP_EMBED_URL = f"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d310.5!2d{LON}!3d{LAT}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5m2!1sru!2s"

# Alternative simpler format (using query parameter)
# MAP_EMBED_URL = f"https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q={LAT},{LON}&mode=embed"

# Directions link for the button
DIRECTIONS_URL = f"https://www.google.com/maps/dir/?api=1&destination={LAT},{LON}"

# Russian map section HTML
MAP_SECTION_RU = f'''
    <!-- Location Section -->
    <section id="location" class="location" style="background: #f8f5f0; padding: 60px 0;">
      <div class="container">
        <div class="section-header">
          <span class="section-badge">📍 Местоположение</span>
          <h2 class="section-title">Наш адрес</h2>
          <p class="section-subtitle">Кушнет Казма, Куба, Азербайджан</p>
        </div>
        <div class="map-container" style="position: relative; background: #F4EBD9; border-radius: 20px; overflow: hidden; height: 400px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); margin-top: 30px;">
          <a href="{DIRECTIONS_URL}" target="_blank" class="map-link" style="display: block; width: 100%; height: 100%; text-decoration: none;">
            <iframe 
              src="{MAP_EMBED_URL}"
              width="100%" 
              height="400" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
            <div class="map-overlay" style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 10;">
              <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/></svg>
              Построить маршрут
            </div>
          </a>
        </div>
        <div style="text-align: center; margin-top: 30px;">
          <p style="font-size: 1.1rem; color: #1F2937;"><strong>📍 Кушнет Казма, Куба, Азербайджан</strong></p>
          <p style="color: #6b7280; margin-top: 10px;">{LAT}° N, {LON}° E</p>
        </div>
      </div>
    </section>
'''

try:
    # Connect to FTP
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    # Files to process
    files = [
        ("quba.rent/index-ru.html", "index-ru.html"),
        ("quba.rent/index-en.html", "index-en.html"),
        ("quba.rent/index-ar.html", "index-ar.html"),
    ]

    for remote_path, local_name in files:
        print(f"\n--- Processing {local_name} ---")
        
        # Download file
        with open(local_name, 'wb') as f:
            ftp.retrbinary(f'RETR {remote_path}', f.write)
        print(f"✓ Downloaded: {local_name}")
        
        # Read and find the old map section
        with open(local_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the map section
        import re
        
        # Pattern to match the old map container with iframe
        old_map_pattern = r'<div class="map-container"[^>]*>.*?<iframe[^>]*>.*?</iframe>.*?</div>'
        
        # New map container HTML
        new_map_container = f'''<div class="map-container" style="position: relative; background: #F4EBD9; border-radius: 20px; overflow: hidden; height: 400px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); margin-top: 30px;">
          <a href="{DIRECTIONS_URL}" target="_blank" class="map-link" style="display: block; width: 100%; height: 100%; text-decoration: none;">
            <iframe 
              src="{MAP_EMBED_URL}"
              width="100%" 
              height="400" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
            <div class="map-overlay" style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 10;">
              <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/></svg>
              Построить маршрут
            </div>
          </a>
        </div>'''
        
        # Replace the old iframe with new one
        new_content = re.sub(old_map_pattern, new_map_container, content, flags=re.DOTALL)
        
        # Write modified content
        with open(local_name, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated map section in: {local_name}")
        
        # Upload back to server
        with open(local_name, 'rb') as f:
            ftp.storbinary(f'STOR {remote_path}', f)
        print(f"✓ Uploaded: {local_name}")

    # Close FTP connection
    ftp.quit()
    print("\n✓ All files processed successfully!")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
