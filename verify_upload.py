#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

REMOTE_PATH = '/quba.rent/index-en.html'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected! Downloading file to verify...")
    
    # Download the file content
    lines = []
    ftp.retrlines(f'RETR {REMOTE_PATH}', lines.append)
    
    content = '\n'.join(lines)
    
    # Check for the floating widget
    has_floating_widget = 'id="booking-widget"' in content
    has_trigger_button = 'class="booking-trigger-btn"' in content
    has_open_function = 'function openBookingWidget()' in content
    has_close_function = 'function closeBookingWidget()' in content
    
    print("\nVerification Results:")
    print(f"  ✓ Floating widget div: {has_floating_widget}")
    print(f"  ✓ Trigger button: {has_trigger_button}")
    print(f"  ✓ Open function: {has_open_function}")
    print(f"  ✓ Close function: {has_close_function}")
    
    # Check that the static section was removed
    has_static_section = 'id="booking-widget-section"' in content
    
    if not has_static_section:
        print(f"  ✓ Static section removed: True")
    else:
        print(f"  ⚠ Static section removed: False (still present)")
    
    if all([has_floating_widget, has_trigger_button, has_open_function, has_close_function]):
        print("\n✅ All changes verified successfully!")
    else:
        print("\n❌ Some changes are missing!")
