#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add 'www.Quba.rent' watermark to ALL images in all HTML files.
"""

import os
import re
from pathlib import Path

def add_watermark_to_html(file_path):
    """Add watermark div wrapper to all images in an HTML file."""
    
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if watermark styles already exist
    if '.image-watermark' in content:
        print(f"  ✓ Watermark styles already exist in {file_path.name}")
        images_found = 0
        for match in re.finditer(r'<img[^>]*>', content):
            images_found += 1
        
        if images_found > 0:
            # Check if images are already wrapped
            if '<div class="image-watermark">' in content:
                print(f"  ✓ Images already wrapped in {file_path.name}")
                return True
        
        if images_found == 0:
            print(f"  ℹ No images found in {file_path.name}")
            return True
    
    # Add watermark styles before </style> tag
    watermark_styles = '''
    .image-watermark {
      position: relative;
      display: block;
    }
    .image-watermark img {
      display: block;
    }
    .watermark {
      position: absolute;
      bottom: 15px;
      right: 15px;
      background: rgba(0, 0, 0, 0.6);
      color: white;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 600;
      font-family: 'Noto Sans', sans-serif;
      z-index: 10;
      backdrop-filter: blur(4px);
    }'''
    
    # Find the style section and add watermark styles
    style_pattern = r'(</style>)'
    if re.search(style_pattern, content):
        content = re.sub(style_pattern, watermark_styles + r'\n    \1', content)
        print(f"  ✓ Added watermark styles to {file_path.name}")
    else:
        # Add to head section
        head_pattern = r'(</head>)'
        if re.search(head_pattern, content):
            content = re.sub(head_pattern, f'<style>{watermark_styles}</style>\n    \1', content)
            print(f"  ✓ Added watermark styles to head of {file_path.name}")
    
    # Wrap each image with watermark div
    # Pattern to match img tags that are NOT already wrapped
    img_pattern = r'(<img[^>]*src="[^"]*"[^>]*>)'
    
    def wrap_image(match):
        img_tag = match.group(1)
        
        # Skip images that are already wrapped
        if 'image-watermark' in img_tag or 'watermark' in img_tag:
            return match.group(0)
        
        # Add class="watermark-img" to img tag to prevent double wrapping
        if 'class=' in img_tag:
            img_tag = re.sub(r'class="([^"]*)"', r'class="\1 watermark-img"', img_tag)
        else:
            img_tag = img_tag[:-1] + ' class="watermark-img">'
        
        return f'<div class="image-watermark">\n      {img_tag}\n      <div class="watermark">www.Quba.rent</div>\n    </div>'
    
    # Apply wrapping
    wrapped_count = 0
    new_content = content
    
    # Find all img tags
    img_tags = re.findall(img_pattern, content)
    
    for img_tag in img_tags:
        if 'image-watermark' not in img_tag and 'watermark-img' not in img_tag:
            wrapped_img_tag = img_tag
            # Add class to prevent double wrapping
            if 'class=' in wrapped_img_tag:
                wrapped_img_tag = re.sub(r'class="([^"]*)"', r'class="\1 watermark-img"', wrapped_img_tag)
            else:
                wrapped_img_tag = wrapped_img_tag[:-1] + ' class="watermark-img">'
            
            wrapped = f'<div class="image-watermark">\n      {wrapped_img_tag}\n      <div class="watermark">www.Quba.rent</div>\n    </div>'
            new_content = new_content.replace(img_tag, wrapped, 1)
            wrapped_count += 1
    
    if wrapped_count > 0:
        print(f"  ✓ Wrapped {wrapped_count} images in {file_path.name}")
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Process all HTML files in the workspace."""
    
    html_files = list(Path('/workspace').glob('*.html'))
    
    print("=" * 60)
    print("Adding 'www.Quba.rent' watermark to ALL photos")
    print("=" * 60)
    print(f"\nFound {len(html_files)} HTML files\n")
    
    for html_file in sorted(html_files):
        print(f"Processing: {html_file.name}")
        add_watermark_to_html(html_file)
        print()
    
    print("=" * 60)
    print("✓ All HTML files updated successfully!")
    print("=" * 60)

if __name__ == '__main__':
    main()
