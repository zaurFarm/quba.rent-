#!/usr/bin/env python3
"""
FTP Upload Script for index-en.html
Uploads the modified English language file to the server
"""

import ftplib
import os

# FTP Configuration
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'

# File to upload
LOCAL_FILE = '/workspace/quba.rent/index-en.html'
REMOTE_FILE = 'index-en.html'

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
                # Store the file directly in root
                ftp.storbinary(f'STOR {REMOTE_FILE}', f)
            
            print(f"Successfully uploaded {REMOTE_FILE} to FTP root!")
            
            # Verify the file exists
            files = ftp.nlst()
            print(f"Files in root: {files}")
            
            if REMOTE_FILE in files:
                print(f"✓ File {REMOTE_FILE} is now on the server!")
            else:
                print(f"✗ Warning: File {REMOTE_FILE} not found in listing")
                
    except ftplib.error_perm as e:
        print(f"FTP Permission Error: {e}")
    except ftplib.error_temp as e:
        print(f"FTP Temporary Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    upload_file()
