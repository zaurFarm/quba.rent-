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
    
    # Check if /az/ directory exists
    try:
        ftp.cwd('/az')
        print("✓ /az/ directory EXISTS on server")
        print(f"Current directory: {ftp.pwd()}")
        
        # List files in /az/
        print("\nFiles in /az/:")
        files = ftp.nlst()
        for f in files:
            print(f"  {f}")
        
        # Download index.html from /az/
        print("\n📥 Downloading index.html from /az/...")
        lines = []
        ftp.retrlines('RETR index.html', lines.append)
        content = '\n'.join(lines)
        
        # Check the booking widget structure
        has_floating_widget = 'id="booking-widget"' in content
        has_section_widget = 'id="booking-widget-section"' in content
        has_trigger_button = 'booking-trigger-btn' in content
        has_open_function = 'openBookingWidget' in content
        has_close_function = 'closeBookingWidget' in content
        
        print("\n📊 Widget Analysis for /az/index.html:")
        print(f"  Floating widget div: {has_floating_widget}")
        print(f"  Static section widget: {has_section_widget}")
        print(f"  Trigger button: {has_trigger_button}")
        print(f"  Open function: {has_open_function}")
        print(f"  Close function: {has_close_function}")
        
        # Save the file locally for inspection
        with open('/workspace/quba.rent/az_index_downloaded.html', 'w') as f:
            f.write(content)
        print(f"\n✅ Saved /az/index.html to /workspace/quba.rent/az_index_downloaded.html")
        
    except ftplib.error_perm as e:
        print(f"✗ /az/ directory does NOT exist or access denied: {e}")
