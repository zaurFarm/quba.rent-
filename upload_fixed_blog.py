#!/usr/bin/env python3
"""
Upload fixed blog.html to server via FTP
"""
from ftplib import FTP
import os

def upload_file():
    # FTP credentials
    host = "95.216.232.219"
    port = 19121
    login = "www-data"
    password = "0R6dXU1YnwSEl1OnURos"
    
    local_file = "/workspace/blog.html"
    remote_file = "quba.rent/blog.html"
    
    print(f"Uploading {local_file} to {remote_file}...")
    
    try:
        with FTP() as ftp:
            ftp.connect(host, port)
            ftp.login(login, password)
            ftp.cwd("quba.rent")
            
            # Upload the file
            with open(local_file, 'rb') as f:
                ftp.storbinary(f"STOR {remote_file}", f)
            
            print("✓ File uploaded successfully!")
            
    except Exception as e:
        print(f"✗ Error uploading file: {e}")

if __name__ == "__main__":
    upload_file()
