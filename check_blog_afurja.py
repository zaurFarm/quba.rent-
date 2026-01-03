#!/usr/bin/env python3
import ftplib
import os
import glob

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print("Connecting to FTP...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("✓ Connected to FTP")
    
    # Download the existing blog-afurja-ru.html
    print("\n--- Downloading existing article ---")
    with open('/workspace/blog-afurja-ru.html', 'wb') as f:
        ftp.retrbinary('RETR quba.rent/blog-afurja-ru.html', f.write)
    print("✓ Downloaded blog-afurja-ru.html")

print("\n--- Files in workspace ---")
# Check workspace for downloaded images
for ext in ['*.jpg', '*.jpeg', '*.png']:
    files = glob.glob(f'/workspace/{ext}')
    for f in files:
        print(f"  {os.path.basename(f)}")
