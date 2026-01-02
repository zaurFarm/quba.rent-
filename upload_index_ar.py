#!/usr/bin/env python3
"""
FTP Upload Script for index-ar.html
Uploads the modified Arabic language file to the server
"""

import ftplib

# FTP Configuration
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'

# File to upload
LOCAL_FILE = '/workspace/quba.rent/index-ar.html'
REMOTE_FILE = 'index-ar.html'

def upload_file():
    """Upload the file to FTP server"""
    try:
        print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")
        
        # Connect to FTP server
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASSWORD)
            print("Connected successfully!")
            
            # Change to root directory
            ftp.cwd('/')
            print(f"Current directory: {ftp.pwd()}")
            
            # Read local file and upload
            print(f"Uploading {LOCAL_FILE}...")
            with open(LOCAL_FILE, 'rb') as f:
                ftp.storbinary(f'STOR {REMOTE_FILE}', f)
            
            print(f"Successfully uploaded {REMOTE_FILE} to FTP root!")
            
    except ftplib.error_perm as e:
        print(f"FTP Permission Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    upload_file()
