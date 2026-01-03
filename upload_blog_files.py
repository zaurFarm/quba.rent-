from ftplib import FTP
import os

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

# Files to upload
files_to_upload = [
    {
        "local_path": "/workspace/blog-red-village-ru.html",
        "remote_path": "quba.rent/blog-red-village-ru.html"
    },
    {
        "local_path": "/workspace/blog-red-village-culture.jpg",
        "remote_path": "quba.rent/images/blog-red-village-culture.jpg"
    },
    {
        "local_path": "/workspace/blog-red-village-city.jpg",
        "remote_path": "quba.rent/images/blog-red-village-city.jpg"
    },
    {
        "local_path": "/workspace/blog-red-village-mountains.jpg",
        "remote_path": "quba.rent/images/blog-red-village-mountains.jpg"
    }
]

try:
    # Connect to FTP
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    for file_info in files_to_upload:
        local_path = file_info["local_path"]
        remote_path = file_info["remote_path"]

        # Check if local file exists
        if not os.path.exists(local_path):
            print(f"✗ File not found: {local_path}")
            continue

        # Upload file
        with open(local_path, 'rb') as f:
            ftp.storbinary(f'STOR {remote_path}', f)

        print(f"✓ Uploaded: {local_path} -> {remote_path}")

    # Close FTP connection
    ftp.quit()
    print("\n✓ All files uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
