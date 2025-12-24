#!/bin/bash

# FTP credentials
FTP_HOST="95.216.232.219"
FTP_PORT="19121"
FTP_USER="www-data"
FTP_PASS="0R6dXU1YnwSEl1OnURos"

# Files to upload
FILES=("index.html" "index-en.html" "index-ru.html" "index-ar.html")

echo "Загрузка обновленных файлов на сервер..."

for file in "${FILES[@]}"; do
    echo "Загружаем $file..."
    
    # Upload file to FTP server
    curl -T "$file" "ftp://${FTP_HOST}:${FTP_PORT}/var/www/quba.rent/${file}" \
        --user "${FTP_USER}:${FTP_PASS}" \
        --progress-bar
    
    if [ $? -eq 0 ]; then
        echo "✅ $file успешно загружен"
    else
        echo "❌ Ошибка загрузки $file"
    fi
    echo ""
done

echo "Загрузка завершена!"