#!/usr/bin/env python3
import ftplib
from PIL import Image, ImageDraw, ImageFont
import os
import re

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'

# Local paths
LOCAL_DIR = "/workspace"
IMAGES_DIR = f"{LOCAL_DIR}/imgs"
OUTPUT_DIR = f"{LOCAL_DIR}/output"

def create_watermarked_image(source_path, output_path, watermark_text="Quba.Rent"):
    """Create an image with watermark"""
    try:
        with Image.open(source_path) as img:
            # Create a copy
            result = img.copy()
            width, height = result.size
            
            # Create watermark overlay
            watermark = Image.new('RGBA', result.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)
            
            # Add text watermark
            try:
                font_size = int(height * 0.04)
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
            except:
                font = ImageFont.load_default()
            
            # Get text size
            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Position (bottom-right corner with padding)
            padding = int(width * 0.03)
            x = width - text_width - padding - 10
            y = height - text_height - padding - 10
            
            # Semi-transparent background
            bg_padding = 10
            draw.rectangle(
                [x - bg_padding, y - bg_padding, x + text_width + bg_padding, y + text_height + bg_padding],
                fill=(255, 255, 255, 160)
            )
            
            # Draw text
            draw.text((x, y), watermark_text, font=font, fill=(47, 82, 51, 200))
            
            # Paste watermark
            result.paste(watermark, (0, 0), watermark)
            
            # Save
            if result.mode != 'RGB':
                result = result.convert('RGB')
            result.save(output_path, 'JPEG', quality=95)
            return True
    except Exception as e:
        print(f"Error creating watermark for {source_path}: {e}")
        return False

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process Afurja waterfall images
print("--- Processing Afurja waterfall images ---")
afurja_images = [
    ("afurja-waterfall-quba-azerbaijan-cliff-view.jpg", "blog-afurja-main.jpg"),
    ("afurja-waterfall-quba-azerbaijan-cliff.jpg", "blog-afurja-detail.jpg"),
]

for source, target in afurja_images:
    source_path = os.path.join(IMAGES_DIR, source)
    target_path = os.path.join(OUTPUT_DIR, target)
    
    if os.path.exists(source_path):
        if create_watermarked_image(source_path, target_path):
            print(f"✓ Created: {target}")
    else:
        print(f"✗ Source not found: {source_path}")

print("\n--- Images ready for upload ---")
