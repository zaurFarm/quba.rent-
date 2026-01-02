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
    
    # Check what files exist in root
    print("\n📂 Checking all HTML files on server...")
    all_files = ftp.nlst()
    
    html_files = [f for f in all_files if f.endswith('.html')]
    print(f"Found {len(html_files)} HTML files:")
    for f in html_files:
        print(f"  {f}")
    
    # Check if index.php exists (WordPress)
    php_files = [f for f in all_files if f.endswith('.php')]
    if php_files:
        print(f"\n⚠️ Found {len(php_files)} PHP files (WordPress detected):")
        for f in php_files[:10]:  # Show first 10
            print(f"  {f}")
        if len(php_files) > 10:
            print(f"  ... and {len(php_files) - 10} more")
    
    # Check if there's a WordPress index that might be overriding HTML
    print("\n🔍 Checking for index files...")
    for f in all_files:
        if 'index' in f.lower():
            print(f"  {f}")
    
    # Try to find /az/ directory
    print("\n🔍 Looking for /az/ variations...")
    
    # Check main index.html content
    print("\n📄 Checking main index.html on server...")
    lines = []
    ftp.retrlines('RETR index.html', lines.append)
    content = '\n'.join(lines)
    
    # Check widget structure
    has_floating = 'id="booking-widget"' in content
    has_section = 'id="booking-widget-section"' in content
    has_trigger = 'booking-trigger-btn' in content
    has_open = 'function openBookingWidget' in content
    has_close = 'function closeBookingWidget' in content
    
    print(f"\n📊 Widget Analysis for index.html:")
    print(f"  Floating widget div: {has_floating}")
    print(f"  Static section: {has_section}")
    print(f"  Trigger button: {has_trigger}")
    print(f"  Open function: {has_open}")
    print(f"  Close function: {has_close}")
    
    if has_floating and has_trigger:
        print("\n✅ index.html has CORRECT widget structure")
    else:
        print("\n❌ index.html widget is BROKEN or MISSING!")
        print("   Need to re-upload the correct version!")
