#!/usr/bin/env python3
"""
Create watermarked images for Red Village article from user-provided photos
"""
from PIL import Image
import os

def create_watermarked_image(input_path, output_path, logo_path, width=1200):
    """
    Create a watermarked version of an image
    
    Args:
        input_path: Path to source image
        output_path: Path to save watermarked image
        logo_path: Path to logo/watermark file
        width: Target width for the image
    """
    print(f"Processing: {input_path}")
    
    try:
        # Open the base image
        img = Image.open(input_path)
        
        # Convert to RGB if necessary (for PNG with transparency)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Calculate new height to maintain aspect ratio
        w_percent = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        # Open and prepare logo
        logo = Image.open(logo_path)
        
        # Resize logo to be 10-15% of image width
        logo_width = int(width * 0.15)
        logo_aspect = logo.height / logo.width
        logo_height = int(logo_width * logo_aspect)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Apply transparency to logo
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Create a white overlay for better visibility
        overlay = Image.new('RGBA', logo.size, (255, 255, 255, 0))
        # Blend logo with semi-transparent white
        logo_with_overlay = Image.blend(overlay, logo, 0.7)
        
        # Calculate position (bottom right with 20px margin)
        x = width - logo_width - 20
        y = height - logo_height - 20
        
        # Paste logo onto image
        img.paste(logo_with_overlay, (x, y), logo_with_overlay)
        
        # Save as JPEG
        img.convert('RGB').save(output_path, 'JPEG', quality=85, optimize=True)
        
        print(f"  ✓ Created: {output_path}")
        print(f"    Size: {width}x{height}px")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Creating Watermarked Images for Red Village Article")
    print("=" * 60)
    
    # Paths
    base_path = "/workspace/user_input_files"
    output_path = "/workspace"
    logo_path = "/workspace/quba.rent/favicon.svg"
    
    # Images to process (selected from deep_thinking analysis)
    images = [
        {
            "source": "fc8a6150-a597-402f-b2da-97fe261f571c.jpeg",
            "output": "blog-red-village-new1.jpg",
            "alt": "Живописная природа и лес Гечреш возле Красной Слободы"
        },
        {
            "source": "cfd69f36-2237-43ac-b7aa-874c5fe12fec.jpeg",
            "output": "blog-red-village-new2.jpg",
            "alt": "Традиционный интерьер дома в Красной Слободе с коврами"
        },
        {
            "source": "c40328d5-cca6-42e8-bc63-8f26ff200167.jpeg",
            "output": "blog-red-village-new3.jpg",
            "alt": "Уютная кухня и столовая в гостевом доме Красной Слободы"
        }
    ]
    
    # Convert SVG logo to PNG first
    print("\nPreparing logo...")
    try:
        from cairosvg import svg2png
        import io
        
        with open(logo_path, 'rb') as f:
            svg_content = f.read()
        
        # Convert SVG to PNG
        png_data = svg2png(bytestring=svg_content, output_width=200)
        logo_temp = io.BytesIO(png_data)
        logo_temp_path = "/workspace/temp_logo.png"
        
        with open(logo_temp_path, 'wb') as f:
            f.write(png_data)
        
        print(f"  ✓ Logo converted and saved to temp file")
        
    except Exception as e:
        print(f"  ✗ Error converting logo: {e}")
        return
    
    # Process each image
    print("\nProcessing images...")
    print("-" * 60)
    
    for img_info in images:
        input_file = os.path.join(base_path, img_info["source"])
        output_file = os.path.join(output_path, img_info["output"])
        
        if os.path.exists(input_file):
            create_watermarked_image(input_file, output_file, logo_temp_path)
        else:
            print(f"  ✗ File not found: {input_file}")
    
    # Clean up temp logo
    if os.path.exists(logo_temp_path):
        os.remove(logo_temp_path)
        print("\n  ✓ Temp logo removed")
    
    print("\n" + "=" * 60)
    print("Processing complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
