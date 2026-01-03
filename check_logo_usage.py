#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

# Connect to FTP server
with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected!")
    
    # Download index-ar.html to check logo reference
    print("\n--- Downloading index-ar.html to check logo reference ---")
    with open('/workspace/index-ar-check.html', 'wb') as f:
        ftp.retrbinary('RETR quba.rent/index-ar.html', f.write)
    print("Downloaded index-ar.html")
    
    # Check for any SVG or PNG logo files in root and subdirectories
    print("\n--- Looking for all image files in quba.rent ---")
    ftp.cwd('quba.rent')
    
    all_images = []
    for root, dirs, files in ftp.mlsd():
        for f in files:
            if f.endswith(('.png', '.svg', '.jpg', '.jpeg')):
                full_path = f
                if root != '.':
                    full_path = f"{root}/{f}"
                all_images.append(full_path)
    
    for f in sorted(all_images):
        print(f"  {f}")
