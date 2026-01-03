from ftplib import FTP
import os

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

# Files to upload
files_to_upload = [
    ("/workspace/output/blog-afurja-main.jpg", "quba.rent/images/blog-afurja-main.jpg"),
    ("/workspace/output/blog-afurja-detail.jpg", "quba.rent/images/blog-afurja-detail.jpg"),
]

try:
    # Connect to FTP
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    # Upload images
    print("\n--- Uploading images ---")
    for local_path, remote_path in files_to_upload:
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"✓ Uploaded: {os.path.basename(local_path)}")
        else:
            print(f"✗ File not found: {local_path}")

    ftp.quit()
    print("\n✓ All images uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
