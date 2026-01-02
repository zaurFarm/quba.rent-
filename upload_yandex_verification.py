#!/usr/bin/env python3
"""
FTP Upload Script for Yandex site verification file
Uploads yandex_c80da51a3c27a7e9.html to the server root
"""

import ftplib

# FTP Configuration
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'

# File to upload
LOCAL_FILE = '/workspace/user_input_files/yandex_c80da51a3c27a7e9.html'
REMOTE_FILE = 'yandex_c80da51a3c27a7e9.html'

def upload_file():
    """Upload the Yandex verification file to FTP server"""
    try:
        print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")
        
        # Connect to FTP server
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASSWORD)
            print("✓ Connected successfully!")
            
            # Change to root directory
            ftp.cwd('/')
            print(f"Current directory: {ftp.pwd()}")
            
            # Read local file and upload
            print(f"Uploading {LOCAL_FILE}...")
            with open(LOCAL_FILE, 'rb') as f:
                ftp.storbinary(f'STOR {REMOTE_FILE}', f)
            
            print(f"✓ Successfully uploaded {REMOTE_FILE} to FTP root!")
            
            # Verify the file exists
            files = ftp.nlst()
            if REMOTE_FILE in files:
                print(f"✓ Verification: File {REMOTE_FILE} is now on the server!")
            else:
                print(f"✗ Warning: File {REMOTE_FILE} not found in listing")
                
            # Show the verification URL
            print(f"\n📋 Yandex Verification Details:")
            print(f"   File: {REMOTE_FILE}")
            print(f"   Token: c80da51a3c27a7e9")
            print(f"   Verification URL: https://quba.rent/{REMOTE_FILE}")
                
    except ftplib.error_perm as e:
        print(f"FTP Permission Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    upload_file()
