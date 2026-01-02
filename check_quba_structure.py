#!/usr/bin/env python3
import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected!")
    
    # Check if there's an /az/ directory or if it's handled by .htaccess
    print("\n🔍 Checking for /az/ directory structure...")
    
    # List quba.rent directory
    print("\n📂 Files in /quba.rent/:")
    try:
        ftp.cwd('/quba.rent')
        files = ftp.nlst()
        for f in sorted(files):
            print(f"  {f}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Check for subdirectories
    print("\n📂 Looking for subdirectories...")
    for f in files:
        try:
            ftp.cwd(f)
            print(f"  📁 {f}/")
            ftp.cwd('..')
        except:
            pass  # Not a directory
    
    # Check if there's a WordPress in quba.rent
    print("\n🔍 Checking for WordPress in /quba.rent/...")
    wp_files = ['wp-config.php', 'wp-login.php', 'wp-admin']
    for wp in wp_files:
        try:
            lines = []
            ftp.retrlines(f'RETR {wp}', lines.append)
            print(f"  ⚠️ Found {wp} - WordPress IS installed in quba.rent!")
        except:
            pass
    
    # Check what serves the root URL
    print("\n🔍 Checking index.php in /quba.rent/...")
    try:
        lines = []
        ftp.retrlines('RETR index.php', lines.append)
        print(f"  Found index.php! Size: {len(lines)} lines")
    except ftplib.error_perm:
        print("  No index.php in /quba.rent/")
