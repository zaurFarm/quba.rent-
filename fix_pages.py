#!/usr/bin/env python3
"""
Fix main page styles from Azerbaijani version and remove WhatsApp from Arabic
"""

import re
import ftplib

def fix_main_page():
    """Fix main page by updating about section styles"""
    
    # Read the live Azerbaijani version to get correct styles
    with open('/workspace/quba.rent/az_live.html', 'r', encoding='utf-8') as f:
        az_content = f.read()
    
    # Extract the about section HTML from Azerbaijani version
    about_section_az = '''  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <div class="about-grid">
        <div class="about-content">
          <span class="section-badge">🏡 Ailəvi istirahət üçün ideal yer</span>
          <h2>Küsnet Qazma kəndində ekoloji təmiz məkan</h2>
          <p>Bizim dağ evi Quba rayonunun Küsnet Qazma kəndində yerləşir. Bu möhtəşəm ərazi öz təbiətinin gözəlliyi, çoxlu ağacları və bulaq suyu ilə seçilir. Burada hava həqiqətən təmizdir, səs-küy yoxdur - yalnız quşların oxuması və çayın şırıltısı eşidilir.</p>
          <p style="background:#dcfce7;padding:15px;border-radius:12px;border-left:4px solid #16a34a"><strong style="color:#16a34a">✅ Ailələr üçün nəzərdə tutulub</strong><br><span style="color:#4b5563">Biz yalnız ailəli qonaqları qəbul edirik. Sərxoş qonaqlar və səs-küylü əyləncələr qəbul edilmir. Bu, dinc, təhlükəsiz və rahat istirahət yeridir.</span></p>
          <div class="features-grid">
            <div class="feature-item">
              <div class="feature-icon green">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
                </svg>
              </div>
              <span>Ekoloji təmiz ərazi</span>
            </div>
            <div class="feature-item">
              <div class="feature-icon green">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
                </svg>
              </div>
              <span>Meşə ilə əhatə olunmuş</span>
            </div>
            <div class="feature-item">
              <div class="feature-icon blue">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
                </svg>
              </div>
              <span>Bulaq suyu</span>
            </div>
            <div class="feature-item">
              <div class="feature-icon blue">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9"/>
                </svg>
              </div>
              <span>Dağ mənzərəsi</span>
            </div>
          </div>
        </div>
        <div class="about-images">
          <div class="owner-image-container">
            <img src="images/owner.jpg" alt="Neriman - Ev Sahibi" onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect fill=%22%232F5233%22 width=%22100%22 height=%22100%22/><text x=%2250%22 y=%2255%22 font-size=%2240%22 fill=%22white%22 text-anchor=%22middle%22>N</text></svg>'">
            <div class="owner-caption">👨‍💼 Nəriman - Ev Sahibi</div>
          </div>
        </div>
      </div>
    </div>
  </section>'''
    
    # Read main page
    with open('/workspace/quba.rent/index.html', 'r', encoding='utf-8') as f:
        main_content = f.read()
    
    # Replace the about section
    # First find the current about section
    about_start = main_content.find('<!-- About Section -->')
    about_end = main_content.find('<!-- Gallery Section -->')
    
    if about_start != -1 and about_end != -1:
        # Keep the first part (before about section)
        first_part = main_content[:about_start]
        # Keep the last part (after about section)
        last_part = main_content[about_end:]
        # Combine
        new_content = first_part + about_section_az + last_part
        
        # Save the updated main page
        with open('/workspace/quba.rent/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ Main page about section fixed!")
    else:
        print("❌ Could not find about section in main page")

def fix_arabic_whatsapp():
    """Remove left WhatsApp button from Arabic version"""
    
    # Read Arabic page
    with open('/workspace/quba.rent/index-ar.html', 'r', encoding='utf-8') as f:
        arabic_content = f.read()
    
    # Remove the left WhatsApp button (whatsapp-float class)
    # This removes the entire whatsapp-float div
    whatsapp_float_pattern = r'<!-- WhatsApp Floating Button \(RTL\) -->.*?whatsapp-float">.*?</div>\s*</div>'
    cleaned_content = re.sub(whatsapp_float_pattern, '', arabic_content, flags=re.DOTALL)
    
    # Also remove the style for whatsapp-float from the style section
    style_pattern = r'\.whatsapp-float\{[^}]+[^}]+\}'
    cleaned_content = re.sub(style_pattern, '', cleaned_content)
    
    # Save the cleaned Arabic page
    with open('/workspace/quba.rent/index-ar.html', 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print("✅ Arabic version WhatsApp button removed!")

def upload_files():
    """Upload fixed files to server"""
    FTP_HOST = '95.216.232.219'
    FTP_PORT = 19121
    FTP_USER = 'www-data'
    FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'
    
    files_to_upload = [
        ('/workspace/quba.rent/index.html', 'index.html'),
        ('/workspace/quba.rent/index-ar.html', 'index-ar.html'),
    ]
    
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASSWORD)
            print(f"Connected to {FTP_HOST}:{FTP_PORT}")
            
            for local_file, remote_file in files_to_upload:
                with open(local_file, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_file}', f)
                print(f"✅ Uploaded {remote_file}")
            
    except Exception as e:
        print(f"❌ Error uploading: {e}")

if __name__ == '__main__':
    fix_main_page()
    fix_arabic_whatsapp()
    upload_files()
