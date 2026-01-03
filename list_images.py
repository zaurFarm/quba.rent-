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
    
    # Navigate to quba.rent/images
    try:
        ftp.cwd('quba.rent/images')
        print(f"\nChanged to images directory: {ftp.pwd()}")
        
        # List image files
        print("\nImage files in quba.rent/images:")
        files = ftp.nlst()
        jpg_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        for f in sorted(jpg_files):
            print(f"  {f}")
    except Exception as e:
        print(f"Could not access images directory: {e}")
