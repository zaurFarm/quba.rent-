#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Downloading index-ru.html...")
    with open('/workspace/index-ru-check.html', 'wb') as f:
        ftp.retrbinary('RETR quba.rent/index-ru.html', f.write)
    print("✓ Downloaded index-ru.html")

# Search for map iframe in the file
print("\n--- Searching for map section ---")
with open('/workspace/index-ru-check.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
import re

# Find map-related content
if 'google' in content.lower():
    print("Found 'google' references in the file")
    
# Find iframe with maps
iframes = re.findall(r'<iframe[^>]*>.*?</iframe>', content, re.DOTALL | re.IGNORECASE)
print(f"\n--- Found {len(iframes)} iframe(s) ---")

for i, iframe in enumerate(iframes, 1):
    print(f"\n--- Iframe {i} ---")
    if 'maps' in iframe.lower() or 'google' in iframe.lower():
        print("Map iframe found:")
        print(iframe[:500])
