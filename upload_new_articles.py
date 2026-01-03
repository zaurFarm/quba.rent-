from ftplib import FTP
import os

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

# Files to upload
articles = [
    ("/workspace/output/blog-qechresh-ru.html", "quba.rent/blog-qechresh-ru.html"),
    ("/workspace/output/blog-hynalyg-ru.html", "quba.rent/blog-hynalyg-ru.html"),
]

try:
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    print("\n--- Uploading new articles ---")
    for local_path, remote_path in articles:
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"✓ Uploaded: {os.path.basename(local_path)}")
        else:
            print(f"✗ File not found: {local_path}")

    ftp.quit()
    print("\n✓ All articles uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
