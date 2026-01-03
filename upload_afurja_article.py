from ftplib import FTP

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

try:
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    # Upload updated Afurja article
    print("\n--- Uploading updated Afurja article ---")
    with open('/workspace/output/blog-afurja-ru-new.html', 'rb') as f:
        ftp.storbinary('STOR quba.rent/blog-afurja-ru.html', f)
    print("✓ Uploaded blog-afurja-ru.html")

    ftp.quit()
    print("\n✓ Article uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
