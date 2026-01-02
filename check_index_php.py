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
    
    # Download index.php
    print("\n📄 Downloading index.php from /quba.rent/...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.php', lines.append)
    content = '\n'.join(lines)
    
    print(f"index.php size: {len(content)} bytes")
    print(f"Number of lines: {len(lines)}")
    print("\n📝 Content:")
    print("-" * 60)
    print(content[:500])
    print("-" * 60)
    
    # Check if it's a WordPress file
    if 'wp-blog-header.php' in content or 'wp-load.php' in content:
        print("\n⚠️ This is a WordPress index.php - it loads WordPress!")
        print("   Your static index.html is being ignored!")
        
        # Check .htaccess
        print("\n📄 Checking .htaccess...")
        try:
            lines = []
            ftp.retrlines('RETR /quba.rent/.htaccess', lines.append)
            htcontent = '\n'.join(lines)
            print(f".htaccess size: {len(htcontent)} bytes")
            print("\n📝 .htaccess content:")
            print(htcontent[:500])
            
            # Check if it has rules for index.html
            if 'index.html' in htcontent:
                print("\n✅ .htaccess mentions index.html")
            else:
                print("\n⚠️ .htaccess does NOT mention index.html - it might be serving WordPress first!")
        except Exception as e:
            print(f"Error reading .htaccess: {e}")
