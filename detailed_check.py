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
    
    # Download index.html from server
    print("\n📥 Downloading index.html from /quba.rent/...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.html', lines.append)
    content = '\n'.join(lines)
    
    print(f"Server file size: {len(content)} bytes")
    
    # Count occurrences of key elements
    print("\n📊 Element counts:")
    print(f"  booking-trigger-btn: {content.count('booking-trigger-btn')}")
    print(f"  openBookingWidget: {content.count('openBookingWidget')}")
    print(f"  closeBookingWidget: {content.count('closeBookingWidget')}")
    print(f"  booking-widget: {content.count('booking-widget')}")
    print(f"  Bron et: {content.count('Bron et')}")
    
    # Show the trigger button HTML
    print("\n🔍 Looking for trigger button...")
    trigger_idx = content.find('booking-trigger-btn')
    if trigger_idx > 0:
        snippet = content[max(0, trigger_idx-50):min(len(content), trigger_idx+300)]
        print(f"Found trigger button HTML:\n{snippet}")
    else:
        print("❌ Trigger button NOT FOUND!")
    
    # Show openBookingWidget function
    print("\n🔍 Looking for openBookingWidget function...")
    func_idx = content.find('function openBookingWidget')
    if func_idx > 0:
        snippet = content[func_idx:min(len(content), func_idx+400)]
        print(f"Found function:\n{snippet}")
    else:
        print("❌ Function NOT FOUND!")
