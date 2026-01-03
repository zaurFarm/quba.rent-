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
    
    # Navigate to quba.rent
    ftp.cwd('quba.rent')
    
    # List all .svg files
    print("\n--- SVG files in quba.rent ---")
    files = ftp.nlst()
    svg_files = [f for f in files if f.endswith('.svg')]
    for f in sorted(svg_files):
        print(f"  {f}")
    
    # Check img directory
    print("\n--- SVG files in quba.rent/img ---")
    try:
        ftp.cwd('img')
        files = ftp.nlst()
        svg_files = [f for f in files if f.endswith('.svg')]
        for f in sorted(svg_files):
            print(f"  {f}")
    except Exception as e:
        print(f"Could not access img directory: {e}")
    
    # Download the 1604538.svg which might be the logo
    print("\n--- Downloading potential logo files ---")
    
    svg_files_to_try = ['telegram-robot.svg', '1604538.svg']
    for svg_name in svg_files_to_try:
        try:
            with open(f'/workspace/{svg_name}', 'wb') as f:
                ftp.retrbinary(f'RETR quba.rent/{svg_name}', f.write)
            print(f"✓ Downloaded: {svg_name}")
            
            # Read first few lines to check content
            with open(f'/workspace/{svg_name}', 'r') as f:
                content = f.read(500)
                print(f"  Preview: {content[:200]}...")
        except Exception as e:
            print(f"✗ Could not download {svg_name}: {e}")
