#!/usr/bin/env python3
"""
Add photo-5.jpg (Interior) to all language versions
"""

import ftplib
import re

def add_photo_to_gallery(file_path, alt_text):
    """Add photo-5.jpg to gallery section"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find gallery section and add photo-5.jpg
    # Insert after photo-4.jpg line
    old_pattern = r'(<img src="/images/photo-4\.jpg" alt="River view">)'
    new_line = r'\1\n        <img src="/images/photo-5.jpg" alt="' + alt_text + '">'
    
    content = re.sub(old_pattern, new_line, content)
    
    # Save the fixed file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added photo-5.jpg to {file_path}")

def upload_files():
    """Upload fixed files to server"""
    FTP_HOST = '95.216.232.219'
    FTP_PORT = 19121
    FTP_USER = 'www-data'
    FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'
    
    files = [
        '/workspace/quba.rent/index.html',
        '/workspace/quba.rent/index-ru.html',
        '/workspace/quba.rent/index-en.html',
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
    # Add photo-5 to main AZ page (Daxili = Interior in Azerbaijani)
    add_photo_to_gallery('/workspace/quba.rent/index.html', 'Daxili')
    
    # Add photo-5 to Russian version (Интерьер)
    add_photo_to_gallery('/workspace/quba.rent/index-ru.html', 'Интерьер')
    
    # Add photo-5 to English version (Interior)
    add_photo_to_gallery('/workspace/quba.rent/index-en.html', 'Interior')
    
    # Upload all files
    upload_files()
