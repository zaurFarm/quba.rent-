#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

# Connect to FTP server
with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected!")
    
    # Check if blog article exists
    print("\n--- Checking blog-red-village-ru.html ---")
    ftp.cwd('quba.rent')
    files = ftp.nlst()
    if 'blog-red-village-ru.html' in files:
        print("✓ blog-red-village-ru.html exists on server")
    else:
        print("✗ blog-red-village-ru.html NOT found")
    
    # Check uploaded images
    print("\n--- Checking uploaded blog images ---")
    ftp.cwd('quba.rent/images')
    files = ftp.nlst()
    blog_images = [f for f in files if f.startswith('blog-red-village')]
    for f in sorted(blog_images):
        print(f"  ✓ {f}")
