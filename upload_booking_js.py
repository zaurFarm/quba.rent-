import ftplib

# FTP connection settings
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

# Connect to FTP
print('Подключение к FTP серверу...')
ftp = ftplib.FTP()
ftp.connect(FTP_HOST, FTP_PORT)
ftp.login(FTP_USER, FTP_PASS)

# Navigate to correct directory and upload
try:
    ftp.cwd('/var/www/quba.rent/js')
    print('Директория /var/www/quba.rent/js найдена')
except:
    try:
        # Create directory if it doesn't exist
        ftp.mkd('/var/www/quba.rent/js')
        print('Создана директория /var/www/quba.rent/js')
        ftp.cwd('/var/www/quba.rent/js')
    except Exception as e:
        print(f'Ошибка: {e}')

# Upload booking.js
try:
    with open('/workspace/quba.rent/js/booking.js', 'rb') as f:
        ftp.storbinary('STOR booking.js', f)
    print('✓ Загружен: js/booking.js')
except Exception as e:
    print(f'✗ Ошибка: {e}')

ftp.quit()
