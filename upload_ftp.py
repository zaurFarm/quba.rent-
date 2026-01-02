#!/usr/bin/env python3
import ftplib
import os

# FTP credentials
HOST = '95.216.232.219'
PORT = 19121
USERNAME = 'www-data'
PASSWORD = '0R6dXU1YnwSEl1OnURos'

FILE_PATH = '/workspace/quba.rent/index.html'
REMOTE_PATH = '/quba.rent/index.html'

# Upload file
with ftplib.FTP() as ftp:
    ftp.connect(HOST, PORT)
    ftp.login(USERNAME, PASSWORD)
    
    with open(FILE_PATH, 'rb') as f:
        ftp.storbinary(f'STOR {REMOTE_PATH}', f)
    
    print('File uploaded successfully!')
