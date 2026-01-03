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
    
    # Check for logo files in quba.rent root
    print("\n--- Files in quba.rent root (looking for logo) ---")
    ftp.cwd('quba.rent')
    files = ftp.nlst()
    logo_files = [f for f in files if 'logo' in f.lower() or f.endswith('.png')]
    for f in sorted(logo_files):
        print(f"  {f}")
    
    # Also check img directory
    print("\n--- Files in quba.rent/img directory ---")
    try:
        ftp.cwd('img')
        files = ftp.nlst()
        for f in sorted(files):
            print(f"  {f}")
    except Exception as e:
        print(f"Could not access img directory: {e}")
