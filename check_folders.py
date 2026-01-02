#!/usr/bin/env python3
import ftplib

# FTP credentials
host = '95.216.232.219'
port = 19121
username = 'www-data'
password = '0R6dXU1YnwSEl1OnURos'

print("Checking server directory structure...")

try:
    with ftplib.FTP() as ftp:
        ftp.connect(host, port)
        ftp.login(username, password)
        
        # List root directory
        print("\nRoot directory contents:")
        ftp.retrlines('LIST', print)
        
        # Check if en, ru, ar directories exist
        for folder in ['en', 'ru', 'ar']:
            try:
                ftp.cwd(f'public_html/{folder}')
                print(f"\n✅ Folder public_html/{folder} exists")
                ftp.cwd('/')  # Go back to root
            except Exception:
                print(f"\n❌ Folder public_html/{folder} does NOT exist")
        
except Exception as e:
    print(f"Error: {e}")
