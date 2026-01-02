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
    
    # Download and check index.html
    print("\n📄 Checking index.html on server...")
    lines = []
    ftp.retrlines('RETR index.html', lines.append)
    content = '\n'.join(lines)
    
    print(f"File size: {len(content)} bytes")
    
    # Check ALL widget components
    checks = {
        'Floating widget div (id="booking-widget")': 'id="booking-widget"' in content,
        'Widget header with "Qısa Bron"': 'booking-widget-header' in content and 'Qısa Bron' in content,
        'Close button (closeBookingWidget)': 'closeBookingWidget' in content,
        'Trigger button (booking-trigger-btn)': 'booking-trigger-btn' in content,
        'Open function (openBookingWidget)': 'function openBookingWidget' in content,
        'Close function (closeBookingWidget)': 'function closeBookingWidget' in content,
        'No static section (booking-widget-section)': 'id="booking-widget-section"' not in content,
        'Booking form with sendBookingToWhatsApp': 'sendBookingToWhatsApp' in content,
        'WhatsApp button text': 'WhatsApp ilə Bron Et' in content,
    }
    
    print("\n📊 COMPLETE WIDGET CHECKLIST:")
    print("=" * 60)
    all_pass = True
    for check, result in checks.items():
        status = "✅" if result else "❌"
        print(f"  {status} {check}")
        if not result:
            all_pass = False
    
    print("=" * 60)
    if all_pass:
        print("🎉 ALL COMPONENTS PRESENT - WIDGET IS WORKING!")
    else:
        print("⚠️ SOME COMPONENTS MISSING - WIDGET MAY NOT WORK!")
    
    # Show trigger button HTML
    print("\n🔍 Searching for trigger button HTML...")
    if 'booking-trigger-btn' in content:
        idx = content.find('booking-trigger-btn')
        snippet = content[max(0, idx-50):min(len(content), idx+200)]
        print(f"Found trigger button HTML:\n{snippet}...")
    
    # Show JS functions
    print("\n🔍 Searching for openBookingWidget function...")
    if 'function openBookingWidget' in content:
        idx = content.find('function openBookingWidget')
        snippet = content[idx:idx+300]
        print(f"Found openBookingWidget function:\n{snippet}...")
