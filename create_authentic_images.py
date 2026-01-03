#!/usr/bin/env python3
"""
Create watermarked images from authentic Red Village photos
"""
from PIL import Image
import os

def create_watermarked_image(input_path, output_path, logo_path, width=1200):
    """Create a watermarked version of an image"""
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
        logo_width = int(width * 0.12)
        logo_aspect = logo.height / logo.width
        logo_height = int(logo_width * logo_aspect)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # Apply transparency to logo
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Create a white overlay for better visibility
        overlay = Image.new('RGBA', logo.size, (255, 255, 255, 0))
        # Blend logo with semi-transparent white
        logo_with_overlay = Image.blend(overlay, logo, 0.65)
        
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
    print("Creating Watermarked Images - Authentic Red Village")
    print("=" * 60)
    
    # Paths
    base_path = "/workspace/user_input_files"
    output_path = "/workspace"
    logo_path = "/workspace/quba.rent/favicon.svg"
    
    # Selected authentic images (from deep_thinking analysis)
    images = [
        {
            "source": "image.png",
            "output": "blog-red-village-authentic1.jpg",
            "alt": "Историческая панорама Еврейской Слободы начала XX века"
        },
        {
            "source": "image_1.png",
            "output": "blog-red-village-authentic2.jpg",
            "alt": "Арочный мост через реку Кудиалчай и долина"
        },
        {
            "source": "image_3.png",
            "output": "blog-red-village-authentic3.jpg",
            "alt": "Улица Красной Слободы с традиционной застройкой"
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
        
        print(f"  ✓ Logo converted")
        
    except Exception as e:
        print(f"  ✗ Error converting logo: {e}")
        return
    
    # Process each image
    print("\nProcessing authentic images...")
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
        print("\n  ✓ Cleanup complete")
    
    print("\n" + "=" * 60)
    print("Processing complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
