#!/usr/bin/env python3
"""
Verify all language versions have the correct static booking widget
"""

import ftplib

FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASSWORD = '0R6dXU1YnwSEl1OnURos'

FILES = ['index.html', 'index-en.html', 'index-ru.html', 'index-ar.html']

def check_file_content(ftp, filename):
    """Download and check if file has the static widget"""
    try:
        print(f"\n{'='*60}")
        print(f"Checking {filename}...")
        print('='*60)
        
        # Download file content
        content = []
        ftp.retrlines(f'RETR {filename}', content.append)
        html = '\n'.join(content)
        
        # Check for new static widget indicators
        checks = {
            'Has new static widget section': '<section class="booking-section"' in html or 'booking-widget-container' in html,
            'Has name input field': 'id="booking-name"' in html,
            'Has responsive styles': '@media (max-width: 768px)' in html,
            'Has handleBookingSubmit function': 'function handleBookingSubmit(event)' in html,
            'Has no old floating widget trigger': 'booking-trigger-btn' not in html,
            'Has no old openBookingWidget function': 'function openBookingWidget' not in html,
        }
        
        all_passed = True
        for check_name, check_result in checks.items():
            status = "✓ PASS" if check_result else "✗ FAIL"
            print(f"  {status}: {check_name}")
            if not check_result:
                all_passed = False
        
        return all_passed
        
    except ftplib.error_perm as e:
        print(f"  ✗ ERROR: Permission denied - {e}")
        return False
    except Exception as e:
        print(f"  ✗ ERROR: {e}")
        return False

def main():
    print("="*60)
    print("BOOKING WIDGET VERIFICATION")
    print("="*60)
    
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASSWORD)
            ftp.cwd('/')
            print(f"Connected to {FTP_HOST}:{FTP_PORT}")
            print(f"Current directory: {ftp.pwd()}")
            
            results = {}
            for filename in FILES:
                results[filename] = check_file_content(ftp, filename)
            
            print("\n" + "="*60)
            print("SUMMARY")
            print("="*60)
            
            passed = sum(1 for v in results.values() if v)
            total = len(results)
            
            for filename, result in results.items():
                status = "✓ PASS" if result else "✗ FAIL"
                print(f"  {status}: {filename}")
            
            print(f"\nTotal: {passed}/{total} files passed verification")
            
            if passed == total:
                print("\n🎉 ALL FILES VERIFIED SUCCESSFULLY!")
                print("The static booking widget is properly configured across all language versions.")
            else:
                print("\n⚠️ Some files need attention!")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == '__main__':
    main()
