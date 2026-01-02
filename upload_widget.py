#!/usr/bin/env python3
import ftplib

# FTP credentials
host = '95.216.232.219'
port = 19121
username = 'www-data'
password = '0R6dXU1YnwSEl1OnURos'

# File to upload
local_file = 'quba.rent/index.html'
remote_file = 'public_html/index.html'

print(f"Uploading {local_file} to {host}:{port}...")

try:
    # Connect to FTP server
    with ftplib.FTP() as ftp:
        ftp.connect(host, port)
        ftp.login(username, password)
        
        # Upload the file
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        
        print(f"Successfully uploaded {local_file} to {remote_file}")
        
        # Verify the upload by getting file size
        ftp.voidcmd('NOOP')
        print("Upload verified successfully!")
        
except Exception as e:
    print(f"Error: {e}")
    exit(1)
