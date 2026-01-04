#!/usr/bin/env python3
"""
Fix booking buttons to use local anchors (#booking instead of /#booking)
"""
import os
from pathlib import Path

def fix_booking_buttons():
    # Define which HTML files are part of the main site
    main_files = [
        'blog-ru.html',
        'blog-en.html',
        'blog-ar.html',
        'blog.html',
        'index-ru.html',
        'index-en.html',
        'index-ar.html',
        'blog-afurja-ru.html',
        'quba.rent/index-ru.html',
        'quba.rent/index-en.html',
        'quba.rent/index-ar.html',
        'quba.rent/index.html',
        'quba.rent/blog-ru.html',
        'quba.rent/blog-en.html',
        'quba.rent/blog-ar.html',
        'quba.rent/blog.html',
        'quba.rent/tours-ru.html',
        'quba.rent/tours-en.html',
        'quba.rent/tours-ar.html',
        'quba.rent/tours.html',
        'quba-cottage/public/index-ru.html',
        'quba-cottage/public/index-en.html',
        'quba-cottage/public/index-ar.html',
        'quba-cottage/public/index.html',
        'quba-cottage/public/blog-ru.html',
        'quba-cottage/public/blog-en.html',
        'quba-cottage/public/blog-ar.html',
        'quba-cottage/public/blog.html',
        'quba-cottage/public/tours-ru.html',
        'quba-cottage/public/tours-en.html',
        'quba-cottage/public/tours-ar.html',
        'quba-cottage/public/tours.html',
    ]
    
    fixed_count = 0
    processed_files = []
    
    for filename in main_files:
        if not os.path.exists(filename):
            continue
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count occurrences before
        old_count = content.count('href="/#booking"')
        old_count_alt = content.count('href=\"/#booking\"')
        total_old = old_count + old_count_alt
        
        if total_old > 0:
            # Replace all /#booking with #booking (local anchors)
            content = content.replace('href="/#booking"', 'href="#booking"')
            content = content.replace('href=\"/#booking\"', 'href="#booking"')
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            fixed_count += total_old
            processed_files.append((filename, total_old))
    
    print("=" * 60)
    print("✓ Booking buttons fixed!")
    print("=" * 60)
    print(f"  Changed: {fixed_count} buttons across {len(processed_files)} files")
    print(f"  Now using: local anchors (#booking)")
    print("=" * 60)
    
    if processed_files:
        print("\nModified files:")
        for filename, count in processed_files:
            print(f"  ✓ {filename}: {count} button(s)")

if __name__ == "__main__":
    fix_booking_buttons()
