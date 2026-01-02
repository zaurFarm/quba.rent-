#!/usr/bin/env python3
"""
Script to fix Arabic version issues:
1. Remove WhatsApp floating button from left side
2. Ensure proper section closure
"""

# Read the Arabic HTML file
with open('/workspace/quba.rent/index-ar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the WhatsApp floating button section (lines 1738-1746 in original)
# This is the div with class="whatsapp-float" for RTL
import re

# Remove the WhatsApp floating button completely (RTL version)
whatsapp_float_pattern = r'<!-- WhatsApp Floating Button \(RTL\) -->\s*<div class="whatsapp-float">.*?</div>'
content = re.sub(whatsapp_float_pattern, '', content, flags=re.DOTALL)

# Also remove the WhatsApp popup button (RTL version)
whatsapp_popup_pattern = r'<!-- WhatsApp Popup Button \(RTL\) -->\s*<div class="whatsapp-popup">.*?</div>'
content = re.sub(whatsapp_popup_pattern, '', content, flags=re.DOTALL)

# Fix the Amenities section - ensure proper closing
# The Amenities section might be missing a closing </section> tag
content = content.replace(
    '    </section>\n\n  <!-- Booking Widget Section',
    '    </section>\n  </section>\n\n  <!-- Booking Widget Section'
)

# Ensure there's a proper section closure before booking widget
# Find the Amenities section end and add closing tags if needed
if '</section>\n</section>' not in content and '</section>\n    </div>\n  </section>' not in content:
    # Add proper closure
    content = content.replace(
        '</section>\n\n  <!-- Booking Widget Section - Above Footer -->',
        '</section>\n    </div>\n  </section>\n\n  <!-- Booking Widget Section - Above Footer -->'
    )

# Write the fixed content back
with open('/workspace/quba.rent/index-ar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Arabic version:")
print("- Removed WhatsApp floating button")
print("- Removed WhatsApp popup button")
print("- Ensured proper section closures")
