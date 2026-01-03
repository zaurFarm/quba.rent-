#!/usr/bin/env python3
"""
Upload fixed blog.html to server via FTP - with delete and retry logic
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
    remote_file = "blog.html"
    
    print(f"Uploading {local_file} to {remote_file}...")
    
    try:
        with FTP() as ftp:
            ftp.connect(host, port)
            ftp.login(login, password)
            print("Logged in successfully")
            
            # Try to navigate to the correct directory
            try:
                ftp.cwd("quba.rent")
                print("Changed to quba.rent directory")
            except Exception as e:
                print(f"Could not change to quba.rent: {e}")
            
            # List current directory
            print(f"Current directory: {ftp.pwd()}")
            files = ftp.nlst()
            print(f"Files in directory: {files}")
            
            # Try to delete existing file if it exists
            try:
                ftp.delete(remote_file)
                print(f"Deleted existing {remote_file}")
            except Exception as e:
                print(f"File didn't exist or couldn't be deleted: {e}")
            
            # Upload the file
            print(f"Uploading {remote_file}...")
            with open(local_file, 'rb') as f:
                ftp.storbinary(f"STOR {remote_file}", f)
            
            print("✓ File uploaded successfully!")
            return True
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    upload_file()
