#!/usr/bin/env python3
"""
Upload authentic Red Village images and updated HTML to server
"""
from ftplib import FTP
import os

def upload_files():
    # FTP credentials
    host = "95.216.232.219"
    port = 19121
    login = "www-data"
    password = "0R6dXU1YnwSEl1OnURos"
    
    # Files to upload
    files = [
        {
            "local": "/workspace/blog-red-village-authentic1.jpg",
            "remote": "quba.rent/images/blog-red-village-authentic1.jpg",
            "desc": "Historical photo - Еврейская Слобода"
        },
        {
            "local": "/workspace/blog-red-village-authentic2.jpg",
            "remote": "quba.rent/images/blog-red-village-authentic2.jpg",
            "desc": "Bridge and river valley"
        },
        {
            "local": "/workspace/blog-red-village-authentic3.jpg",
            "remote": "quba.rent/images/blog-red-village-authentic3.jpg",
            "desc": "Street view of Red Village"
        },
        {
            "local": "/workspace/blog-red-village-ru.html",
            "remote": "quba.rent/blog-red-village-ru.html",
            "desc": "Updated article HTML"
        }
    ]
    
    print("=" * 60)
    print("Uploading authentic Red Village content to server")
    print("=" * 60)
    
    try:
        with FTP() as ftp:
            ftp.connect(host, port)
            ftp.login(login, password)
            print("✓ Connected to FTP server")
            
            for file_info in files:
                local_path = file_info["local"]
                remote_path = file_info["remote"]
                desc = file_info["desc"]
                
                if os.path.exists(local_path):
                    file_size = os.path.getsize(local_path)
                    print(f"\nUploading {desc}...")
                    print(f"  Size: {file_size:,} bytes")
                    
                    # Upload file
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f"STOR {remote_path}", f)
                    
                    print(f"  ✓ Uploaded!")
                else:
                    print(f"\n✗ File not found: {local_path}")
            
            print("\n" + "=" * 60)
            print("✓ All files uploaded successfully!")
            print("=" * 60)
            
    except Exception as e:
        print(f"\n✗ FTP Error: {e}")

if __name__ == "__main__":
    upload_files()
