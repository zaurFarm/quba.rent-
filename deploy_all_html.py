#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deploy ALL updated HTML files to the FTP server.
"""

from ftplib import FTP
from pathlib import Path

def deploy_all_files():
    """Upload all HTML files to the FTP server."""
    
    # FTP connection settings
    host = '95.216.232.219'
    port = 19121
    username = 'www-data'
    password = '0R6dXU1YnwSEl1OnURos'
    
    # Get all HTML files
    html_files = list(Path('/workspace').glob('*.html'))
    
    print(f"Connecting to FTP server {host}:{port}...")
    
    try:
        # Connect and login
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print("✓ Connected to FTP server\n")
        
        uploaded_count = 0
        skipped_count = 0
        
        for html_file in sorted(html_files):
            remote_file = html_file.name
            
            # Check if file exists on server
            try:
                ftp.size(remote_file)
                file_exists = True
            except:
                file_exists = False
            
            print(f"Uploading {remote_file}...")
            with open(html_file, 'rb') as f:
                ftp.storbinary(f'STOR {remote_file}', f)
            print(f"  ✓ Uploaded: {remote_file}")
            uploaded_count += 1
        
        # Quit FTP connection
        ftp.quit()
        print(f"\n✓ FTP connection closed")
        print(f"\n{'=' * 60}")
        print(f"✓ Deployment complete!")
        print(f"  Total files uploaded: {uploaded_count}")
        print(f"{'=' * 60}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error during FTP deployment: {e}")
        return False

if __name__ == '__main__':
    deploy_all_files()
