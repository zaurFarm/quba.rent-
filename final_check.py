#!/usr/bin/env python3
import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print("=" * 70)
print("FINAL VERIFICATION - Booking Widget")
print("=" * 70)

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Check index.html
    print("\n📄 Checking index.html...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.html', lines.append)
    html_content = '\n'.join(lines)
    
    html_checks = {
        'Widget HTML (id="booking-widget")': 'id="booking-widget"' in html_content,
        'Trigger Button HTML': 'booking-trigger-btn' in html_content,
        'Open Function': 'function openBookingWidget' in html_content,
        'Close Function': 'function closeBookingWidget' in html_content,
        'Close Button': 'closeBookingWidget()' in html_content,
        'Button Text "Bron et"': 'Bron et' in html_content,
        'Booking Form': 'booking-form' in html_content,
        'WhatsApp Integration': 'sendBookingToWhatsApp' in html_content,
    }
    
    print("\n📊 HTML Components:")
    all_html_pass = True
    for check, result in html_checks.items():
        status = "✅" if result else "❌"
        print(f"  {status} {check}")
        if not result:
            all_html_pass = False
    
    # Check styles.css
    print("\n📄 Checking styles.css...")
    lines = []
    ftp.retrlines('RETR /quba.rent/styles.css', lines.append)
    css_content = '\n'.join(lines)
    
    css_checks = {
        '.booking-widget': '.booking-widget {' in css_content,
        '.booking-trigger-btn': '.booking-trigger-btn {' in css_content,
        '.booking-widget-close': '.booking-widget-close {' in css_content,
        'position: fixed': 'position: fixed' in css_content,
        'display: none': 'display: none' in css_content,
        'bottom: 20px': 'bottom: 20px' in css_content,
    }
    
    print("\n📊 CSS Components:")
    all_css_pass = True
    for check, result in css_checks.items():
        status = "✅" if result else "❌"
        print(f"  {status} {check}")
        if not result:
            all_css_pass = False
    
    print("\n" + "=" * 70)
    if all_html_pass and all_css_pass:
        print("🎉 ALL COMPONENTS PRESENT - WIDGET IS READY!")
        print("\n📝 How to use:")
        print("   1. Open https://quba.rent/ or https://quba.rent/az/")
        print("   2. You should see a 'Bron et' button in the bottom-right corner")
        print("   3. Click the button to open the booking widget")
        print("   4. The widget can be closed with the '✕' button")
        print("\n⚠️ If widget doesn't appear:")
        print("   - Clear browser cache (Ctrl+Shift+R)")
        print("   - Try incognito/private mode")
        print("   - Check browser console for errors (F12)")
    else:
        print("❌ SOME COMPONENTS MISSING - NEEDS FIX!")
    print("=" * 70)
