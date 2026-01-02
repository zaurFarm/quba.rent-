#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected!")
    
    # Download .htaccess file
    print("\n📥 Downloading .htaccess...")
    lines = []
    ftp.retrlines('RETR .htaccess', lines.append)
    content = '\n'.join(lines)
    
    # Save locally
    with open('/workspace/quba.rent/.htaccess', 'w') as f:
        f.write(content)
    
    print("✅ Saved .htaccess to local file")
    print(f"\nFile size: {len(content)} bytes")
    print("\nFirst 100 lines:")
    for i, line in enumerate(lines[:100]):
        print(f"{i+1:3}: {line}")
