#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("--- Downloading blog files to check links ---")
    
    # Download main blog pages
    files_to_download = [
        'quba.rent/blog.html',
        'quba.rent/blog-ru.html', 
        'quba.rent/blog-en.html',
        'quba.rent/blog-ar.html',
    ]
    
    for remote_file in files_to_download:
        local_name = remote_file.replace('quba.rent/', '')
        try:
            with open(f'/workspace/{local_name}', 'wb') as f:
                ftp.retrbinary(f'RETR {remote_file}', f.write)
            print(f"✓ Downloaded: {local_name}")
        except Exception as e:
            print(f"✗ Error downloading {local_name}: {e}")

print("\n--- Files downloaded successfully ---")
