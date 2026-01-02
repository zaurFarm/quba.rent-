#!/usr/bin/env python3
import ftplib

# FTP credentials
FTP_HOST = '95.216.232.219'
FTP_PORT = 19121
FTP_USER = 'www-data'
FTP_PASS = '0R6dXU1YnwSEl1OnURos'

FILES_TO_VERIFY = [
    ('/quba.rent/index-en.html', 'English'),
    ('/quba.rent/index-ru.html', 'Russian'),
    ('/quba.rent/index-ar.html', 'Arabic'),
]

print("=" * 60)
print("VERIFICATION OF BOOKING WIDGET CHANGES")
print("=" * 60)

with ftplib.FTP() as ftp:
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    
    all_passed = True
    
    for remote_path, lang_name in FILES_TO_VERIFY:
        print(f"\n{'=' * 60}")
        print(f"Verifying {lang_name} version: {remote_path}")
        print('=' * 60)
        
        # Download the file content
        lines = []
        ftp.retrlines(f'RETR {remote_path}', lines.append)
        content = '\n'.join(lines)
        
        # Check for the floating widget
        has_floating_widget = 'id="booking-widget"' in content
        has_trigger_button = 'class="booking-trigger-btn"' in content
        has_open_function = 'function openBookingWidget()' in content
        has_close_function = 'function closeBookingWidget()' in content
        
        # Check that the static section was removed
        has_static_section = 'id="booking-widget-section"' in content
        
        # Check for specific translations
        if lang_name == 'English':
            has_correct_translation = '📅 Quick Booking' in content and 'Book via WhatsApp' in content
        elif lang_name == 'Russian':
            has_correct_translation = '📅 Быстрое бронирование' in content and 'Забронировать через WhatsApp' in content
        else:  # Arabic
            has_correct_translation = '📅 الحجز السريع' in content and 'احجز عبر واتساب' in content
        
        print(f"\n  ✓ Floating widget div: {has_floating_widget}")
        print(f"  ✓ Trigger button: {has_trigger_button}")
        print(f"  ✓ Open function: {has_open_function}")
        print(f"  ✓ Close function: {has_close_function}")
        print(f"  ✓ Static section removed: {not has_static_section}")
        print(f"  ✓ Correct translation: {has_correct_translation}")
        
        if all([has_floating_widget, has_trigger_button, has_open_function, 
                has_close_function, not has_static_section, has_correct_translation]):
            print(f"\n  ✅ {lang_name} version: ALL CHECKS PASSED!")
        else:
            print(f"\n  ❌ {lang_name} version: SOME CHECKS FAILED!")
            all_passed = False

print("\n" + "=" * 60)
if all_passed:
    print("🎉 ALL LANGUAGE VERSIONS VERIFIED SUCCESSFULLY!")
    print("The booking widget is now a floating/dismissible widget on all pages.")
else:
    print("⚠️ SOME ISSUES FOUND - Please review the results above")
print("=" * 60)
