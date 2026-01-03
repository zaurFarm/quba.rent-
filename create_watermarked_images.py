from ftplib import FTP
import os
from PIL import Image, ImageDraw, ImageFont

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

local_dir = "/workspace"
server_dir = "quba.rent"
images_dir = f"{server_dir}/images"

try:
    # Connect to FTP
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    # Download source images from server
    print("\n--- Downloading source images ---")
    source_images = [
        ("quba.rent/images/photo-culture.jpg", "photo-culture.jpg"),
        ("quba.rent/images/photo-city.jpg", "photo-city.jpg"),
        ("quba.rent/images/photo-1.jpg", "photo-1.jpg"),
    ]

    downloaded_files = []
    for remote_path, local_name in source_images:
        local_path = os.path.join(local_dir, local_name)
        try:
            with open(local_path, 'wb') as f:
                ftp.retrbinary(f'RETR {remote_path}', f.write)
            print(f"✓ Downloaded: {local_name}")
            downloaded_files.append(local_name)
        except Exception as e:
            print(f"✗ Error downloading {local_name}: {e}")

    # Convert SVG logo to PNG for use as watermark
    print("\n--- Converting logo to PNG ---")
    
    # Read SVG content
    with open('/workspace/favicon.svg', 'r') as f:
        svg_content = f.read()
    
    # For simplicity, create a simple text-based logo or use existing photo
    # Since PIL doesn't directly support SVG, we'll create a simple colored box with text
    # Or we can use one of the existing images as watermark
    
    # Alternative: Create a simple semi-transparent watermark
    print("Note: Using image-based watermark approach")
    
    # Create blog images with watermark
    print("\n--- Creating blog images with watermark ---")

    # Image mappings for blog post - culturally relevant images
    image_mappings = [
        ("photo-culture.jpg", "blog-red-village-culture.jpg", "Культура"),
        ("photo-city.jpg", "blog-red-village-city.jpg", "Город"),
        ("photo-1.jpg", "blog-red-village-mountains.jpg", "Природа"),
    ]

    for source_name, target_name, label in image_mappings:
        source_path = os.path.join(local_dir, source_name)
        target_path = os.path.join(local_dir, target_name)

        if not os.path.exists(source_path):
            print(f"✗ Source file not found: {source_name}")
            continue

        # Open source image
        with Image.open(source_path) as base_img:
            # Create a copy to work with
            img = base_img.copy()
            width, height = img.size

            # Create watermark - semi-transparent white box with text
            watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)

            # Add watermark text/label
            text = "Quba.Rent"
            try:
                # Try to use a font, fallback to default
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(height * 0.05))
            except:
                font = ImageFont.load_default()

            # Get text size
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Position for watermark (bottom-right corner)
            padding = int(width * 0.03)
            x = width - text_width - padding - 10
            y = height - text_height - padding - 10

            # Draw semi-transparent background
            bg_padding = 10
            draw.rectangle(
                [x - bg_padding, y - bg_padding, x + text_width + bg_padding, y + text_height + bg_padding],
                fill=(255, 255, 255, 160)
            )

            # Draw text
            draw.text((x, y), text, font=font, fill=(47, 82, 51, 200))

            # Paste watermark onto image
            img.paste(watermark, (0, 0), watermark)

            # Save watermarked image
            img.convert('RGB').save(target_path, 'JPEG', quality=95)
            print(f"✓ Created: {target_name}")

    # Upload all files to server
    print("\n--- Uploading files to server ---")

    # Upload watermarked images
    for _, target_name, _ in image_mappings:
        local_path = os.path.join(local_dir, target_name)
        if os.path.exists(local_path):
            remote_path = f"{images_dir}/{target_name}"
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"✓ Uploaded: {target_name}")

    # Close FTP connection
    ftp.quit()
    print("\n✓ All files uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
