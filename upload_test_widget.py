#!/usr/bin/env python3
import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

LOCAL_FILE = '/workspace/quba.rent/test-widget.html'
REMOTE_PATH = '/quba.rent/test-widget.html'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected! Uploading test-widget.html...")
    
    with open(LOCAL_FILE, 'rb') as f:
        ftp.storbinary(f'STOR {REMOTE_PATH}', f)
    
    print(f"✅ Uploaded to {REMOTE_PATH}")
    
    # Verify
    size = ftp.size(REMOTE_PATH)
    local_size = os.path.getsize(LOCAL_FILE)
    print(f"Server size: {size} bytes, Local size: {local_size} bytes")
    
    if size == local_size:
        print("✅ Upload verified!")
    else:
        print("❌ Size mismatch!")

import os
