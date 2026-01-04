#!/usr/bin/env python3
import re

# Read the file
with open('blog-red-village-ru.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the pattern to match the entire background property for .cta-section
# The SVG data-uri is very long, so we'll use a regex pattern
pattern = r'\.cta-section\s*\{[^}]*background:\s*url\([^)]+\)[^;]*;[^}]*\}'

# Check if the pattern exists
if re.search(pattern, content):
    # Replace with the new background
    new_background = '''.cta-section {
      background: url('cta_bg.png') center/cover;
      color: white;
      padding: 60px 20px;
      text-align: center;'''
    
    # We need to be more specific - let's replace just the background line
    content = re.sub(
        r'(background:\s*)url\([^)]+\),?\s*linear-gradient[^;]*;',
        r"\1url('cta_bg.png') center/cover;",
        content
    )
    
    # Write the file
    with open('blog-red-village-ru.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully updated the .cta-section background")
else:
    print("Pattern not found in the file")
