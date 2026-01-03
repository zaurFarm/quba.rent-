#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deploy the updated blog-red-village-ru.html to the FTP server.
"""

from ftplib import FTP
import os

def deploy_file():
    """Upload the fixed HTML file to the FTP server."""
    
    # FTP connection settings
    host = '95.216.232.219'
    port = 19121
    username = 'www-data'
    password = '0R6dXU1YnwSEl1OnURos'
    
    # File paths
    local_file = '/workspace/blog-red-village-ru.html'
    remote_file = 'blog-red-village-ru.html'
    
    print(f"Connecting to FTP server {host}:{port}...")
    
    try:
        # Connect and login
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print("✓ Connected to FTP server")
        
        # Upload the file (using STOR command)
        print(f"Uploading {local_file}...")
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        print(f"✓ Successfully uploaded {remote_file}")
        
        # Quit FTP connection
        ftp.quit()
        print("✓ FTP connection closed")
        
        return True
        
    except Exception as e:
        print(f"✗ Error during FTP deployment: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Deploying updated HTML file to server")
    print("=" * 60)
    
    if deploy_file():
        print("\n✓ Deployment successful!")
        print("  The Google Maps iframe has been updated on the server.")
        print("  - Satellite view should now display correctly")
        print("  - Centered on Krasnaya Sloboda coordinates")
    else:
        print("\n✗ Deployment failed")
        exit(1)
