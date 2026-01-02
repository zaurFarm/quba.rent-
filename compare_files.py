#!/usr/bin/env python3
"""
This script checks if the issue is with PHP redirector or the HTML file itself.
The PHP file reads index.html and serves it, so we need to verify it's doing this correctly.
"""

import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

# First, let's check if there's a discrepancy between what's in index.html and what PHP serves

print("=" * 70)
print("COMPARISON: Local index.html vs Server index.html")
print("=" * 70)

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Get local file size
    local_size = 93138  # from our last upload
    print(f"Local index.html size: {local_size} bytes")
    
    # Get server file size
    server_size = ftp.size('/quba.rent/index.html')
    print(f"Server index.html size: {server_size} bytes")
    
    if local_size == server_size:
        print("✅ File sizes match - content should be identical!")
    else:
        print(f"❌ File size mismatch! Difference: {abs(local_size - server_size)} bytes")
        print("   The server file is being modified or replaced!")
    
    # Download server index.html
    print("\n📥 Downloading server index.html for comparison...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.html', lines.append)
    server_content = '\n'.join(lines)
    
    # Read local index.html
    with open('/workspace/quba.rent/index.html', 'r') as f:
        local_content = f.read()
    
    print(f"Local file size: {len(local_content)} bytes")
    print(f"Server file size: {len(server_content)} bytes")
    
    # Check for key elements in both
    print("\n📊 Element comparison:")
    elements = [
        'booking-trigger-btn',
        'openBookingWidget',
        'closeBookingWidget',
        'Bron et',
        'Qısa Bron'
    ]
    
    for elem in elements:
        local_count = local_content.count(elem)
        server_count = server_content.count(elem)
        status = "✅" if local_count == server_count else "❌"
        print(f"  {status} '{elem}': local={local_count}, server={server_count}")
    
    # Show a sample of what PHP serves vs original
    print("\n🔍 Sample of booking widget from server file:")
    idx = server_content.find('booking-trigger-btn')
    if idx > 0:
        snippet = server_content[idx:idx+200]
        print(f"{snippet}...")
    
    # Check if there's a widget div with display:none
    print("\n🔍 Checking widget visibility:")
    if 'display: none' in server_content:
        print("✅ Widget is hidden (display: none) - this is correct!")
        print("   It should appear when clicking 'Bron et' button")
    else:
        print("❌ Widget display style not found!")
