#!/usr/bin/env python3
import ftplib
import os

# FTP credentials
host = '95.216.232.219'
port = 19121
username = 'www-data'
password = '0R6dXU1YnwSEl1OnURos'

# Files to upload
files = [
    # Main website files
    ('quba.rent/index.html', 'public_html/index.html'),
    ('quba.rent/index-en.html', 'index-en.html'),
    ('quba.rent/index-ru.html', 'index-ru.html'),
    ('quba.rent/index-ar.html', 'index-ar.html'),
    ('quba.rent/robots.txt', 'robots.txt'),
    ('quba.rent/sitemap.xml', 'sitemap.xml'),
    ('quba.rent/sitemap-az.xml', 'sitemap-az.xml'),
    ('quba.rent/sitemap-en.xml', 'sitemap-en.xml'),
    ('quba.rent/sitemap-ru.xml', 'sitemap-ru.xml'),
    ('quba.rent/sitemap-ar.xml', 'sitemap-ar.xml'),
    # Blog and tours files
    ('quba.rent/blog.html', 'blog.html'),
    ('quba.rent/blog-en.html', 'blog-en.html'),
    ('quba.rent/blog-ru.html', 'blog-ru.html'),
    ('quba.rent/blog-ar.html', 'blog-ar.html'),
    ('quba.rent/tours.html', 'tours.html'),
    ('quba.rent/tours-en.html', 'tours-en.html'),
    ('quba.rent/tours-ru.html', 'tours-ru.html'),
    ('quba.rent/tours-ar.html', 'tours-ar.html'),
    # Config files
    ('quba.rent/favicon.svg', 'favicon.svg'),
    ('quba.rent/site.webmanifest', 'site.webmanifest'),
]

print("🚀 Uploading SEO-optimized website to server...")

try:
    with ftplib.FTP() as ftp:
        ftp.connect(host, port)
        ftp.login(username, password)

        uploaded = 0
        skipped = 0
        
        for local_file, remote_file in files:
            if os.path.exists(local_file):
                with open(local_file, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_file}', f)
                print(f"✅ {local_file} → /{remote_file}")
                uploaded += 1
            else:
                print(f"⚠️ File not found: {local_file}")
                skipped += 1

        print(f"\n🎉 Successfully uploaded {uploaded} files!")
        if skipped > 0:
            print(f"⚠️ Skipped {skipped} files (not found)")

except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
