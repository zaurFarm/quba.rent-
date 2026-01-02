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
    
    # Download /quba.rent/index.html
    print("\n📥 Downloading /quba.rent/index.html...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.html', lines.append)
    content = '\n'.join(lines)
    
    print(f"File size: {len(content)} bytes")
    
    # Check ALL widget components
    checks = {
        'Floating widget div': 'id="booking-widget"' in content,
        'Widget header': 'booking-widget-header' in content,
        'Close button': 'closeBookingWidget' in content,
        'Trigger button': 'booking-trigger-btn' in content,
        'Open function': 'function openBookingWidget' in content,
        'Close function': 'function closeBookingWidget' in content,
        'Booking form': 'booking-form' in content,
        'Send to WhatsApp': 'sendBookingToWhatsApp' in content,
        'Qısa Bron text': 'Qısa Bron' in content,
        'Bron et text': 'Bron et' in content,
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
        print("⚠️ SOME COMPONENTS MISSING!")
