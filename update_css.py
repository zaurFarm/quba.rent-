#!/usr/bin/env python3
import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

print(f"Connecting to {FTP_HOST}:{FTP_PORT}...")

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("Connected!")
    
    # Download styles.css
    print("\n📥 Downloading styles.css...")
    lines = []
    ftp.retrlines('RETR /quba.rent/styles.css', lines.append)
    css_content = '\n'.join(lines)
    print(f"Original size: {len(css_content)} bytes")
    
    # Add missing widget CSS before </style> or at the end
    widget_css = '''

/* Floating Widget Styles */
.booking-widget {
  position: fixed;
  right: 20px;
  bottom: 100px;
  z-index: 999;
  width: 380px;
  max-width: calc(100vw - 40px);
  background: linear-gradient(135deg, var(--forest) 0%, #1a3a20 100%);
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.booking-widget-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  background: rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.booking-widget-badge {
  color: #fff;
  font-weight: 700;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  gap: 10px;
}

.booking-widget-close {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.booking-widget-close:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* Trigger Button */
.booking-trigger-btn {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 997;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 24px;
  background: linear-gradient(135deg, var(--forest) 0%, #1a3a20 100%);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

.booking-trigger-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.25);
}

.booking-trigger-btn svg {
  width: 20px;
  height: 20px;
}
'''
    
    # Append the widget CSS
    new_css_content = css_content + widget_css
    print(f"New size: {len(new_css_content)} bytes")
    
    # Save locally for backup
    with open('/workspace/quba.rent/styles.css', 'w') as f:
        f.write(new_css_content)
    print("✅ Saved updated styles.css locally")
    
    # Upload to server
    print("\n📤 Uploading updated styles.css...")
    with open('/workspace/quba.rent/styles.css', 'rb') as f:
        ftp.storbinary('STOR /quba.rent/styles.css', f)
    
    print("✅ Uploaded to server!")
    
    # Verify
    server_size = ftp.size('/quba.rent/styles.css')
    print(f"Server file size: {server_size} bytes")
    
    if server_size == len(new_css_content):
        print("✅ CSS upload verified successfully!")
    else:
        print("⚠️ Size mismatch - please check!")
