#!/bin/bash

echo "🚀 Загрузка обновленных файлов на сервер..."
echo "==============================================="

# FTP credentials
FTP_HOST="95.216.232.219"
FTP_PORT="19121"
FTP_USER="www-data"
FTP_PASS="0R6dXU1YnwSEl1OnURos"
LOCAL_DIR="/workspace/quba-cottage/public"
REMOTE_DIR="/var/www/quba.rent"

# Files to upload (основные файлы + туры)
FILES=(
    "index.html"
    "index-en.html" 
    "index-ru.html"
    "index-ar.html"
    "tours.html"
    "tours-en.html"
    "tours-ru.html"
    "tours-ar.html"
)

echo "📁 Загружаемые файлы:"
for file in "${FILES[@]}"; do
    if [ -f "$LOCAL_DIR/$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file (не найден)"
    fi
done

echo ""
echo "📤 Начало загрузки..."

# Загрузка каждого файла
for file in "${FILES[@]}"; do
    if [ -f "$LOCAL_DIR/$file" ]; then
        echo "Загружаем $file..."
        
        # Upload file to FTP server
        curl -T "$LOCAL_DIR/$file" \
             "ftp://$FTP_HOST:$FTP_PORT$REMOTE_DIR/$file" \
             --user "$FTP_USER:$FTP_PASS" \
             --progress-bar \
             --retry 3 \
             --retry-delay 2
        
        if [ $? -eq 0 ]; then
            echo "✅ $file загружен успешно"
        else
            echo "❌ Ошибка загрузки $file"
        fi
        echo ""
    fi
done

echo "🎉 Загрузка завершена!"
echo ""
echo "📋 Что было обновлено:"
echo "- ✅ SEO оптимизация (заголовки, описания, ключевые слова)"
echo "- ✅ Open Graph и Twitter Cards"
echo "- ✅ Schema.org Structured Data (JSON-LD)"
echo "- ✅ Интеграция Calendly для бронирования"
echo "- ✅ Кнопки 'Book Now/Бронирование/حجز' в навигации"
echo "- ✅ Построение маршрута на карте (уже работало)"
echo "- ✅ Мета-теги для геолокации"
echo "- ✅ Hreflang для SEO"
echo ""
echo "🌐 Ваш сайт теперь оптимизирован для SEO Google!"