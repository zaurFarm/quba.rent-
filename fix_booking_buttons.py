#!/usr/bin/env python3
"""
Fix booking buttons to use local anchors (#booking instead of /#booking)
"""
import re

def fix_booking_buttons():
    with open('/workspace/blog-red-village-ru.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count changes
    old_count = content.count('href="/#booking"')
    old_count_alt = content.count('href=\"/#booking\"')
    
    # Replace all /#booking with #booking (local anchors)
    content = content.replace('href="/#booking"', 'href="#booking"')
    content = content.replace('href=\"/#booking\"', 'href="#booking\"')
    
    # Add booking section before CTA section
    booking_section = '''
    <!-- Booking Section Anchor -->
    <div id="booking" style="scroll-margin-top: 100px;"></div>
    '''
    
    content = content.replace(
        '<div class="cta-section">',
        booking_section + '\n\n    <div class="cta-section">'
    )
    
    # Write updated content
    with open('/workspace/blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_count = content.count('href="#booking"')
    
    print("=" * 60)
    print("✓ Booking buttons fixed!")
    print("=" * 60)
    print(f"  Changed: {old_count + old_count_alt} buttons")
    print(f"  Now using: local anchors (#booking)")
    print(f"  Added: Booking section anchor")
    print("=" * 60)

if __name__ == "__main__":
    fix_booking_buttons()
