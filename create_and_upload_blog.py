from ftplib import FTP
import os
from PIL import Image, ImageDraw, ImageFont

# FTP credentials
FTP_HOST = "95.216.232.219"
FTP_PORT = 19121
FTP_USER = "www-data"
FTP_PASSWORD = "0R6dXU1YnwSEl1OnURos"

# Directory structure
local_dir = "/workspace"
server_dir = "quba.rent"
images_dir = f"{server_dir}/images"

# Files to download from server
files_to_download = [
    ("quba.rent/images/photo-1.jpg", "photo-1.jpg"),
    ("quba.rent/images/photo-2.jpg", "photo-2.jpg"),
    ("quba.rent/images/logo.png", "logo.png")
]

# Files to upload after processing
files_to_upload = []

try:
    # Connect to FTP
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASSWORD)
    print("✓ FTP connection established")

    # Download source files
    print("\n--- Downloading source files ---")
    for remote_path, local_name in files_to_download:
        local_path = os.path.join(local_dir, local_name)
        with open(local_path, 'wb') as f:
            ftp.retrbinary(f'RETR {remote_path}', f.write)
        print(f"✓ Downloaded: {local_name}")

    # Create blog images with watermark
    print("\n--- Creating blog images with watermark ---")

    # Image mappings for blog post - using culturally relevant images
    image_mappings = [
        ("photo-culture.jpg", "blog-red-village-culture.jpg"),
        ("photo-city.jpg", "blog-red-village-city.jpg"),
        ("photo-1.jpg", "blog-red-village-mountains.jpg"),
    ]

    for source_name, target_name in image_mappings:
        source_path = os.path.join(local_dir, source_name)
        target_path = os.path.join(local_dir, target_name)

        # Open source image
        with Image.open(source_path) as base_img:
            # Create a copy to work with
            img = base_img.copy()
            width, height = img.size

            # Open logo
            with Image.open(os.path.join(local_dir, "logo.png")) as logo:
                # Resize logo to 15% of image width
                logo_width = int(width * 0.15)
                logo_ratio = logo_width / logo.width
                logo_height = int(logo.height * logo_ratio)
                logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

                # Calculate position (bottom-right corner with padding)
                padding = int(width * 0.02)
                logo_x = width - logo_width - padding
                logo_y = height - logo_height - padding

                # Create transparent overlay for better visibility
                overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
                draw = ImageDraw.Draw(overlay)

                # Semi-transparent background for logo
                bg_width = logo_width + 20
                bg_height = logo_height + 20
                bg_x = logo_x - 10
                bg_y = logo_y - 10
                draw.rectangle([bg_x, bg_y, bg_x + bg_width, bg_y + bg_height],
                              fill=(255, 255, 255, 100))

                # Paste logo onto image
                img.paste(overlay, (0, 0), overlay)
                img.paste(logo, (logo_x, logo_y), logo if logo.mode == 'RGBA' else None)

                # Save watermarked image
                img.convert('RGB').save(target_path, 'JPEG', quality=95)
                print(f"✓ Created: {target_name}")
                files_to_upload.append((target_name, f"{images_dir}/{target_name}"))

    # Upload blog article
    print("\n--- Uploading files to server ---")
    html_file = "blog-red-village-ru.html"
    html_path = os.path.join(local_dir, html_file)

    if os.path.exists(html_path):
        with open(html_path, 'rb') as f:
            ftp.storbinary(f'STOR {server_dir}/{html_file}', f)
        print(f"✓ Uploaded: {html_file}")
    else:
        print(f"✗ HTML file not found: {html_path}")

    # Upload watermarked images
    for local_name, remote_path in files_to_upload:
        local_path = os.path.join(local_dir, local_name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"✓ Uploaded: {local_name} -> {remote_path}")

    # Close FTP connection
    ftp.quit()
    print("\n✓ All files uploaded successfully!")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
