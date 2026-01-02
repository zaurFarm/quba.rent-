#!/usr/bin/env python3
import ftplib
import os

# FTP credentials
host = '95.216.232.219'
port = 19121
username = 'www-data'
password = '0R6dXU1YnwSEl1OnURos'

# Files to upload - directly to root
files = [
    ('quba.rent/index-en.html', 'index-en.html'),
    ('quba.rent/index-ru.html', 'index-ru.html'),
    ('quba.rent/index-ar.html', 'index-ar.html'),
    ('quba.rent/index.html', 'public_html/index.html'),
]

print("Uploading all language versions with new booking widget...")

try:
    with ftplib.FTP() as ftp:
        ftp.connect(host, port)
        ftp.login(username, password)

        for local_file, remote_file in files:
            if os.path.exists(local_file):
                with open(local_file, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_file}', f)
                print(f"✅ Uploaded {local_file} to /{remote_file}")
            else:
                print(f"❌ File not found: {local_file}")

        print("\n✅ All language versions uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
    exit(1)
