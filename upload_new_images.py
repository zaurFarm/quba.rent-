#!/usr/bin/env python3
"""
Upload new images and updated HTML to server via FTP
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
            "local": "/workspace/blog-red-village-new1.jpg",
            "remote": "quba.rent/images/blog-red-village-new1.jpg",
            "desc": "New image 1 (Nature/Forest)"
        },
        {
            "local": "/workspace/blog-red-village-new2.jpg",
            "remote": "quba.rent/images/blog-red-village-new2.jpg",
            "desc": "New image 2 (Traditions/Carpets)"
        },
        {
            "local": "/workspace/blog-red-village-new3.jpg",
            "remote": "quba.rent/images/blog-red-village-new3.jpg",
            "desc": "New image 3 (Hospitality/Kitchen)"
        },
        {
            "local": "/workspace/blog-red-village-ru.html",
            "remote": "quba.rent/blog-red-village-ru.html",
            "desc": "Updated article HTML"
        }
    ]
    
    print("=" * 60)
    print("Uploading files to server")
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
                    print(f"  Local: {local_path}")
                    print(f"  Remote: {remote_path}")
                    print(f"  Size: {file_size:,} bytes")
                    
                    # Upload file
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f"STOR {remote_path}", f)
                    
                    print(f"  ✓ Uploaded successfully!")
                else:
                    print(f"\n✗ File not found: {local_path}")
            
            print("\n" + "=" * 60)
            print("All files uploaded successfully!")
            print("=" * 60)
            
    except Exception as e:
        print(f"\n✗ FTP Error: {e}")

if __name__ == "__main__":
    upload_files()
