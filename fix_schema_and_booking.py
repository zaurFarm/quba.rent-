#!/usr/bin/env python3
"""
Remove amenityFeature from Russian and English versions
Activate booking button to scroll to booking widget
"""

import re

def remove_amenity_feature(file_path):
    """Remove amenityFeature section from HTML file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove amenityFeature section - from "amenityFeature" to the closing bracket
    # Pattern matches amenityFeature array and its contents
    pattern = r'"amenityFeature":\s*\[[^\]]*\]'
    cleaned_content = re.sub(pattern, '"amenityFeature": []', content)
    
    # Save the cleaned file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"✅ amenityFeature removed from {file_path}")

def fix_booking_button(file_path, has_booking_section=True):
    """Fix booking button to scroll to booking widget"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if this file has a booking section
    if 'booking-widget-container' in content or 'booking-section' in content:
        # Find the booking button link and update it to point to #booking
        # The pattern looks for href="#contact" or similar in the hero section
        
        # Replace hero booking button to point to #booking
        content = re.sub(
            r'<a href="#contact" class="cta-btn">',
            '<a href="#booking" class="cta-btn">',
            content
        )
        
        # Also update nav links if they exist
        content = re.sub(
            r'<li><a href="#contact">Контакт</a></li>',
            '<li><a href="#booking">Бронь</a></li>',
            content
        )
        
        # Add booking section anchor if not exists
        if 'id="booking"' not in content:
            # Find the booking widget section and add id
            content = re.sub(
                r'<section class="booking-section"',
                '<section id="booking" class="booking-section"',
                content
            )
    
    # Save the fixed file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Booking button fixed in {file_path}")

def upload_files():
    """Upload fixed files to server"""
    FTP_HOST = '95.216.232.219'
    FTP_PORT = 19121
    FTP_USER = 'www-data'
    FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'
    
    files = [
        '/workspace/quba.rent/index-ru.html',
        '/workspace/quba.rent/index-en.html', 
        '/workspace/quba.rent/index.html',
        '/workspace/quba.rent/index-ar.html',
    ]
    
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASSWORD)
            print(f"Connected to {FTP_HOST}:{FTP_PORT}")
            
            for file_path in files:
                filename = file_path.split('/')[-1]
                with open(file_path, 'rb') as f:
                    ftp.storbinary(f'STOR {filename}', f)
                print(f"✅ Uploaded {filename}")
            
    except Exception as e:
        print(f"❌ Error uploading: {e}")

if __name__ == '__main__':
    # Fix Russian version
    remove_amenity_feature('/workspace/quba.rent/index-ru.html')
    fix_booking_button('/workspace/quba.rent/index-ru.html')
    
    # Fix English version
    remove_amenity_feature('/workspace/quba.rent/index-en.html')
    fix_booking_button('/workspace/quba.rent/index-en.html')
    
    # Fix main page and Arabic version (booking buttons)
    fix_booking_button('/workspace/quba.rent/index.html')
    fix_booking_button('/workspace/quba.rent/index-ar.html')
    
    # Upload all files
    upload_files()
