#!/bin/bash

# FTP Configuration
FTP_HOST="95.216.232.219"
FTP_PORT="19121"
FTP_USER="www-data"
FTP_PASS="0R6dXU1YnwSEl1OnURos"

# Local directory with HTML files
LOCAL_DIR="quba-cottage/public"

# Remote directory (webroot)
REMOTE_DIR="html"

# List of all HTML files to upload
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

echo "================================================"
echo "Uploading files to $REMOTE_DIR/ directory..."
echo "================================================"

for file in "${FILES[@]}"; do
    echo "Uploading: $file..."
    curl --ftp-ssl -k -T "${LOCAL_DIR}/${file}" \
        "ftp://${FTP_USER}:${FTP_PASS}@${FTP_HOST}:${FTP_PORT}/${REMOTE_DIR}/${file}"

    if [ $? -eq 0 ]; then
        echo "✓ Successfully uploaded: $file"
    else
        echo "✗ Failed to upload: $file"
    fi
    echo "----------------------------------------"
done

echo ""
echo "================================================"
echo "Upload complete!"
echo "Testing site availability..."
echo "================================================"

# Test if the site is accessible via HTTP
sleep 2
HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "http://${FTP_HOST}:${FTP_PORT}/${REMOTE_DIR}/index.html" 2>/dev/null || echo "000")

echo "HTTP Response Code: $HTTP_RESPONSE"

if [ "$HTTP_RESPONSE" = "200" ]; then
    echo ""
    echo "✓ SUCCESS! Site is accessible!"
    echo "URL: http://${FTP_HOST}:${FTP_PORT}/${REMOTE_DIR}/index.html"
elif [ "$HTTP_RESPONSE" = "403" ]; then
    echo ""
    echo "✗ Still getting 403 Forbidden error"
    echo "This indicates a permissions issue on the server"
elif [ "$HTTP_RESPONSE" = "000" ]; then
    echo ""
    echo "✗ Could not connect to server"
else
    echo ""
    echo "Response code: $HTTP_RESPONSE"
fi
