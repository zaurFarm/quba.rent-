#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("--- Checking existing blog article files ---")
    ftp.cwd('quba.rent')
    files = ftp.nlst()
    
    # Filter blog articles
    blog_files = [f for f in files if f.startswith('blog-') and f.endswith('.html')]
    
    print("\nAll blog-related files:")
    for f in sorted(blog_files):
        print(f"  ✓ {f}")
    
    # Check specifically for language-specific articles
    print("\n--- Checking article files by language ---")
    
    # Check if -en and -ar versions exist
    articles = ['qechresh', 'red-village', 'afurja', 'hynalyg', 'cuisine', 'chenlibel']
    
    for article in articles:
        print(f"\n{article}:")
        
        # Check Russian
        ru_file = f'blog-{article}-ru.html'
        if ru_file in files:
            print(f"  ✓ {ru_file}")
        else:
            print(f"  ✗ {ru_file} - NOT FOUND")
        
        # Check English
        en_file = f'blog-{article}-en.html'
        if en_file in files:
            print(f"  ✓ {en_file}")
        else:
            print(f"  ✗ {en_file} - NOT FOUND")
        
        # Check Arabic
        ar_file = f'blog-{article}-ar.html'
        if ar_file in files:
            print(f"  ✓ {ar_file}")
        else:
            print(f"  ✗ {ar_file} - NOT FOUND")
