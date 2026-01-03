#!/usr/bin/env python3
"""
Upload updated files to server
"""
from ftplib import FTP
import os

def upload_files():
    host = "95.216.232.219"
    port = 19121
    login = "www-data"
    password = "0R6dXU1YnwSEl1OnURos"
    
    files = [
        {
            "local": "/workspace/blog-red-village-ru.html",
            "remote": "quba.rent/blog-red-village-ru.html",
            "desc": "Updated article with satellite map"
        },
        {
            "local": "/workspace/blog-ru.html",
            "remote": "quba.rent/blog-ru.html",
            "desc": "Blog main page with new images"
        }
    ]
    
    print("=" * 60)
    print("Uploading updated files to server")
    print("=" * 60)
    
    try:
        with FTP() as ftp:
            ftp.connect(host, port)
            ftp.login(login, password)
            print("✓ Connected to FTP server\n")
            
            for file_info in files:
                local_path = file_info["local"]
                remote_path = file_info["remote"]
                desc = file_info["desc"]
                
                if os.path.exists(local_path):
                    file_size = os.path.getsize(local_path)
                    print(f"Uploading: {desc}")
                    print(f"  Size: {file_size:,} bytes")
                    
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f"STOR {remote_path}", f)
                    
                    print(f"  ✓ Uploaded!\n")
                else:
                    print(f"✗ File not found: {local_path}\n")
            
            print("=" * 60)
            print("✓ All files uploaded successfully!")
            print("=" * 60)
            
    except Exception as e:
        print(f"\n✗ FTP Error: {e}")

if __name__ == "__main__":
    upload_files()
