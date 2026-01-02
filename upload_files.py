import ftplib
import os

# FTP connection settings
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

# Files to upload
files_to_upload = [
    ('styles.css', '/workspace/styles.css'),
    ('quba.rent/js/booking.js', '/workspace/quba.rent/js/booking.js')
]

def upload_file(ftp, local_path, remote_path):
    """Upload a single file to FTP server"""
    try:
        with open(local_path, 'rb') as f:
            ftp.storbinary(f'STOR {remote_path}', f)
        print(f'✓ Загружен: {remote_path}')
        return True
    except Exception as e:
        print(f'✗ Ошибка загрузки {remote_path}: {e}')
        return False

# Connect to FTP
print('Подключение к FTP серверу...')
ftp = ftplib.FTP()
ftp.connect(FTP_HOST, FTP_PORT)
ftp.login(FTP_USER, FTP_PASS)
ftp.cwd('/var/www/quba.rent')

# Upload files
success_count = 0
for remote_name, local_path in files_to_upload:
    if upload_file(ftp, local_path, remote_name):
        success_count += 1

# Close connection
ftp.quit()

print(f'\nЗагружено файлов: {success_count}/{len(files_to_upload)}')
