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
    
    # Download index.php - FULL content
    print("\n📄 Downloading FULL index.php...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.php', lines.append)
    content = '\n'.join(lines)
    
    print(f"index.php size: {len(content)} bytes")
    print("\n📝 COMPLETE Content:")
    print("=" * 60)
    print(content)
    print("=" * 60)
