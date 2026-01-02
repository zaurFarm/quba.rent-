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
    
    # Check file dates
    print("\n📅 File modification dates:")
    ftp.voidcmd('TYPE A')
    lines = []
    ftp.retrlines('LIST index.html', lines.append)
    print(f"index.html: {lines[0] if lines else 'not found'}")
    
    # Check index.php
    print("\n🔍 Checking for index.php...")
    try:
        lines = []
        ftp.retrlines('LIST index.php', lines.append)
        print(f"index.php: {lines[0] if lines else 'found but empty'}")
    except:
        print("index.php: NOT FOUND")
    
    # Check wp-admin/index.php (WP dashboard)
    try:
        lines = []
        ftp.retrlines('LIST wp-admin/index.php', lines.append)
        print(f"wp-admin/index.php: EXISTS - WordPress is installed!")
    except Exception as e:
        print(f"wp-admin/index.php: {e}")
    
    # Try to download index.php if it exists
    print("\n📄 Checking index.php content...")
    try:
        lines = []
        ftp.retrlines('RETR index.php', lines.append)
        content = '\n'.join(lines)
        print(f"index.php EXISTS! Size: {len(content)} bytes")
        print("First 200 chars:")
        print(content[:200])
    except ftplib.error_perm as e:
        print(f"index.php: NOT FOUND ({e})")
    
    # Delete the problematic server file and re-upload
    print("\n🔄 Deleting broken index.html from server...")
    try:
        ftp.delete('index.html')
        print("✅ Deleted broken index.html")
    except Exception as e:
        print(f"❌ Could not delete: {e}")
