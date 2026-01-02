#!/usr/bin/env python3
import ftplib
import os

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

# File to upload
LOCAL_FILE = '/workspace/quba.rent/index-ar.html'
REMOTE_PATH = '/quba.rent/index-ar.html'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

# Connect to FTP server
with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected! Uploading index-ar.html...")
    
    # Upload the file
    with open(LOCAL_FILE, 'rb') as f:
        ftp.storbinary(f'STOR {REMOTE_PATH}', f)
    
    print(f"Successfully uploaded to {REMOTE_PATH}")
    
    # Verify the upload
    print("\nVerifying upload...")
    size = ftp.size(REMOTE_PATH)
    print(f"File size on server: {size} bytes")
    
    local_size = os.path.getsize(LOCAL_FILE)
    print(f"Local file size: {local_size} bytes")
    
    if size == local_size:
        print("Upload verified successfully!")
    else:
        print("WARNING: File sizes don't match!")
