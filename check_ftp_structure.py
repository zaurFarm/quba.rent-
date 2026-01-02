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
    print("Current directory:", ftp.pwd())
    
    # List files to understand structure
    print("\nListing directory contents:")
    files = ftp.nlst()
    for f in files[:20]:  # Show first 20 items
        print(f"  {f}")
    
    # Try to find quba.rent directory
    try:
        ftp.cwd('quba.rent')
        print(f"\nChanged to quba.rent directory: {ftp.pwd()}")
        
        # List files in quba.rent
        print("\nFiles in quba.rent:")
        for f in ftp.nlst():
            print(f"  {f}")
    except Exception as e:
        print(f"Could not access quba.rent: {e}")
