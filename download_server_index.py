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
    
    # Download main index.html from server
    print("\n📥 Downloading index.html from server...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.html', lines.append)
    content = '\n'.join(lines)
    
    # Save locally
    with open('/workspace/quba.rent/index_server.html', 'w') as f:
        f.write(content)
    
    print("✅ Saved to /workspace/quba.rent/index_server.html")
    print(f"File size: {len(content)} bytes")
    
    # Check widget structure
    has_floating = 'id="booking-widget"' in content
    has_section = 'id="booking-widget-section"' in content
    has_trigger = 'booking-trigger-btn' in content
    has_open = 'function openBookingWidget' in content
    has_close = 'function closeBookingWidget' in content
    
    print("\n📊 Current Server Widget Analysis:")
    print(f"  Floating widget div: {has_floating}")
    print(f"  Static section: {has_section}")
    print(f"  Trigger button: {has_trigger}")
    print(f"  Open function: {has_open}")
    print(f"  Close function: {has_close}")
    
    if has_floating and has_trigger and has_open and has_close:
        print("\n✅ Widget structure is CORRECT!")
    else:
        print("\n⚠️ Widget structure needs fixes!")
