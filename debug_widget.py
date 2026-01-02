#!/usr/bin/env python3
import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print("=" * 70)
print("DETAILED DEBUGGING - Finding the issue")
print("=" * 70)

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Check index.html on server
    print("\n1️⃣ Checking index.html on server...")
    lines = []
    ftp.retrlines('RETR /quba.rent/index.html', lines.append)
    html = '\n'.join(lines)
    
    # Find booking widget section
    widget_start = html.find('<div id="booking-widget"')
    trigger_start = html.find('<button class="booking-trigger-btn"')
    
    print(f"   Widget starts at position: {widget_start}")
    print(f"   Trigger button at position: {trigger_start}")
    
    if widget_start > 0:
        widget_snippet = html[widget_start:widget_start+500]
        print(f"\n   Widget HTML:\n{widget_snippet}...")
    
    if trigger_start > 0:
        trigger_snippet = html[trigger_start:trigger_start+300]
        print(f"\n   Trigger button HTML:\n{trigger_snippet}...")
    
    # Check styles.css for any conflicting or missing styles
    print("\n2️⃣ Checking styles.css for widget styles...")
    lines = []
    ftp.retrlines('RETR /quba.rent/styles.css', lines.append)
    css = '\n'.join(lines)
    
    # Check if styles are properly defined
    trigger_pos = css.find('.booking-trigger-btn {')
    close_pos = css.find('.booking-widget-close {')
    
    print(f"   .booking-trigger-btn {{ at: {trigger_pos}")
    print(f"   .booking-widget-close {{ at: {close_pos}")
    
    if trigger_pos > 0:
        trigger_css = css[trigger_pos:trigger_pos+400]
        print(f"\n   Trigger button CSS:\n{trigger_css}...")
    
    # Check if CSS has display: flex/block for trigger
    print("\n3️⃣ Checking CSS display properties...")
    if 'display: flex' in css:
        print("   ✅ 'display: flex' found in CSS")
    if 'display: block' in css:
        print("   ✅ 'display: block' found in CSS")
    
    # Find JS functions
    print("\n4️⃣ Checking JavaScript functions...")
    open_pos = html.find('function openBookingWidget')
    close_pos = html.find('function closeBookingWidget')
    
    print(f"   openBookingWidget at: {open_pos}")
    print(f"   closeBookingWidget at: {close_pos}")
    
    if open_pos > 0:
        js_snippet = html[open_pos:open_pos+400]
        print(f"\n   JS Function:\n{js_snippet}...")
    
    # Check if there's any PHP output that might be different
    print("\n5️⃣ Checking for potential issues...")
    
    # Check if HTML has any visible issues
    if '<style>' in html and '</style>' in html:
        style_count = html.count('<style>')
        print(f"   Found {style_count} <style> tags")
    
    if '<script>' in html and '</script>' in html:
        script_count = html.count('<script>')
        print(f"   Found {script_count} <script> tags")
    
    print("\n" + "=" * 70)
