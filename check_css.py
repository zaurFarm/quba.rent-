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
    
    # Check styles.css for booking widget CSS
    print("\n📄 Checking styles.css for widget styles...")
    try:
        lines = []
        ftp.retrlines('RETR /quba.rent/styles.css', lines.append)
        css_content = '\n'.join(lines)
        print(f"styles.css size: {len(css_content)} bytes")
        
        # Check for widget-related CSS
        checks = [
            '.booking-widget {',
            '.booking-trigger-btn {',
            '.booking-widget-close {',
            'position: fixed',
            'display: none',
            'bottom: 20px',
            'right: 20px',
        ]
        
        print("\n📊 CSS Check:")
        for check in checks:
            found = check in css_content
            status = "✅" if found else "❌"
            print(f"  {status} '{check}'")
            
    except Exception as e:
        print(f"Error reading styles.css: {e}")
    
    # Check if styles.css exists and has content
    print("\n📂 Checking CSS and JS files...")
    for f in ['styles.css', 'js/booking.js']:
        try:
            size = ftp.size(f'/quba.rent/{f}')
            print(f"  {f}: {size} bytes")
        except:
            print(f"  {f}: NOT FOUND or empty")
