#!/usr/bin/env python3
import re

# Read the file
with open('blog-red-village-ru.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the .cta-section rule and replace its background property
# We need to handle the complex SVG data URI with escaped characters
# The pattern looks for .cta-section { and then the background line with data URI and gradient
pattern = r'(\.cta-section\s*\{[^}]*background:\s*)url\([^}]+\),?\s*linear-gradient[^;]*;([^}]*\})'

# Check if pattern exists
match = re.search(pattern, content, re.DOTALL)
if match:
    # Replace with the new background
    new_content = match.group(1) + "url('cta_bg.png') center/cover;" + match.group(2)

    # Perform the replacement
    content = re.sub(pattern, new_content, content, flags=re.DOTALL)

    # Write the file
    with open('blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated the .cta-section background")
else:
    print("Pattern not found in the file")
