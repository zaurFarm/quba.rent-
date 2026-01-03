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
    
    # Try to download favicon.svg directly
    print("\n--- Downloading favicon.svg ---")
    try:
        with open('/workspace/favicon.svg', 'wb') as f:
            ftp.retrbinary('RETR favicon.svg', f.write)
        print("✓ Downloaded favicon.svg")
        
        # Read and display content
        with open('/workspace/favicon.svg', 'r') as f:
            content = f.read()
            print(f"File size: {len(content)} bytes")
            print(f"Content preview: {content[:300]}...")
    except Exception as e:
        print(f"Error downloading favicon.svg: {e}")
