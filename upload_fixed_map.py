#!/usr/bin/env python3
"""
Script to upload the updated blog-red-village-ru.html file to the web server.
"""
import ftplib

def upload_updated_file():
    """Upload the fixed HTML file to the server."""
    
    # FTP credentials from system summary
    FTP_HOST = "95.216.232.219"
    FTP_PORT = 19121
    FTP_USER = "www-data"
    FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"
    
    local_file = "/workspace/blog-red-village-ru.html"
    remote_file = "blog-red-village-ru.html"
    
    try:
        # Connect to FTP server
        print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(FTP_USER, FTP_PASSWORD)
        print("Connected successfully!")
        
        # Delete the existing file first (to avoid 553 error)
        print(f"Deleting existing {remote_file}...")
        try:
            ftp.delete(remote_file)
            print("Existing file deleted.")
        except ftplib.error_perm as e:
            print(f"Note: Could not delete file (may not exist): {e}")
        
        # Upload the new file
        print(f"Uploading {local_file}...")
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        print("File uploaded successfully!")
        
        # Close the connection
        ftp.quit()
        print("FTP connection closed.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    upload_updated_file()
