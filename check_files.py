#!/usr/bin/env python3
import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected!")
    
    # List all files
    print("\n📂 All files in root:")
    files = ftp.nlst()
    for f in sorted(files):
        try:
            size = ftp.size(f)
            print(f"  {f}: {size} bytes")
        except:
            print(f"  {f}: (size unknown)")
    
    # Try to access index.html with full path
    print("\n🔍 Checking for index.html...")
    try:
        lines = []
        ftp.retrlines('LIST index.html', lines.append)
        print(f"index.html listing: {lines[0]}")
    except Exception as e:
        print(f"Error listing index.html: {e}")
    
    # Try different path formats
    print("\n🔍 Trying different paths...")
    paths_to_try = [
        'index.html',
        '/index.html',
        '/quba.rent/index.html',
        'quba.rent/index.html',
    ]
    
    for path in paths_to_try:
        try:
            lines = []
            ftp.retrlines(f'LIST {path}', lines.append)
            print(f"  {path}: FOUND - {lines[0]}")
        except Exception as e:
            print(f"  {path}: {e}")
