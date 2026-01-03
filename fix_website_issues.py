#!/usr/bin/env python3
"""
Скрипт для исправления:
1. Названия села: "Кушнет Казма" → "Куснет Газма"
2. Проверки и исправления языковой логики в HTML файлах
"""

import os
import re
import glob

def fix_village_name(content):
    """
    Исправляет название села "Кушнет Казма" на "Куснет Газма"
    """
    # Паттерны для замены (разные варианты неправильного написания)
    replacements = [
        ('Кушнет Казма', 'Куснет Газма'),
        ('Кюснет Казма', 'Куснет Газма'),  # если пользователь хочет именно такой вариант
    ]
    
    changes = 0
    for old, new in replacements:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes += count
    
    return content, changes

def check_language_links(file_path, content):
    """
    Проверяет языковую логику в файле и возвращает список проблем.
    """
    issues = []
    filename = os.path.basename(file_path)
    
    # Определяем язык файла
    lang = 'az'  # по умолчанию
    if '-ru' in filename or filename.startswith('index-ru') or '/ru/' in file_path:
        lang = 'ru'
    elif '-en' in filename or filename.startswith('index-en') or '/en/' in file_path:
        lang = 'en'
    elif '-ar' in filename or filename.startswith('index-ar') or '/ar/' in file_path:
        lang = 'ar'
    
    # Проверяем ссылки на другие страницы
    # Ссылка должна содержать суффикс языка если это перевод
    
    # Проверяем ссылки tours
    if f'tours.html' in content and lang == 'ru' and 'tours-ru.html' not in content:
        issues.append(f"Файл {filename}: отсутствует tours-ru.html (русская версия)")
    if f'tours.html' in content and lang == 'en' and 'tours-en.html' not in content:
        issues.append(f"Файл {filename}: отсутствует tours-en.html (английская версия)")
    if f'tours.html' in content and lang == 'ar' and 'tours-ar.html' not in content:
        issues.append(f"Файл {filename}: отсутствует tours-ar.html (арабская версия)")
    
    # Проверяем ссылки blog
    if f'blog.html' in content and lang == 'ru' and 'blog-ru.html' not in content:
        issues.append(f"Файл {filename}: отсутствует blog-ru.html (русская версия)")
    if f'blog.html' in content and lang == 'en' and 'blog-en.html' not in content:
        issues.append(f"Файл {filename}: отсутствует blog-en.html (английская версия)")
    if f'blog.html' in content and lang == 'ar' and 'blog-ar.html' not in content:
        issues.append(f"Файл {filename}: отсутствует blog-ar.html (арабская версия)")
    
    # Проверяем language switcher
    if 'lang-switch' in content or 'class="lang-btn"' in content:
        # Проверяем, что ссылки на языки корректные
        ru_link = re.search(r'href="[^"]*ru[^"]*"', content)
        az_link = re.search(r'href="[^"]*az[^"]*"', content)
        en_link = re.search(r'href="[^"]*en[^"]*"', content)
        ar_link = re.search(r'href="[^"]*ar[^"]*"', content)
        
        if not ru_link:
            issues.append(f"Файл {filename}: отсутствует ссылка на русскую версию (ru)")
        if not az_link:
            issues.append(f"Файл {filename}: отсутствует ссылка на азербайджанскую версию (az)")
        if not en_link:
            issues.append(f"Файл {filename}: отсутствует ссылка на английскую версию (en)")
        if not ar_link:
            issues.append(f"Файл {filename}: отсутствует ссылка на арабскую версию (ar)")
    
    return issues

def fix_language_links_in_content(content, filename):
    """
    Исправляет ссылки на языковые версии в контенте.
    """
    fixed_content = content
    
    # Для русских файлов - убеждаемся, что ссылки ведут на русские версии
    if '-ru' in filename or 'index-ru' in filename:
        # Заменяем ссылки без языкового суффикса на русские версии
        replacements = [
            ('href="/tours.html"', 'href="/tours-ru.html"'),
            ('href="/blog.html"', 'href="/blog-ru.html"'),
            ('href="/index.html"', 'href="/ru/"'),
            ('href="tours.html"', 'href="tours-ru.html"'),
            ('href="blog.html"', 'href="blog-ru.html"'),
            ('href="index.html"', 'href="index-ru.html"'),
        ]
        
        for old, new in replacements:
            if old in fixed_content:
                fixed_content = fixed_content.replace(old, new)
    
    # Для английских файлов
    elif '-en' in filename or 'index-en' in filename:
        replacements = [
            ('href="/tours.html"', 'href="/tours-en.html"'),
            ('href="/blog.html"', 'href="/blog-en.html"'),
            ('href="/index.html"', 'href="/en/"'),
            ('href="tours.html"', 'href="tours-en.html"'),
            ('href="blog.html"', 'href="blog-en.html"'),
            ('href="index.html"', 'href="index-en.html"'),
        ]
        
        for old, new in replacements:
            if old in fixed_content:
                fixed_content = fixed_content.replace(old, new)
    
    # Для арабских файлов
    elif '-ar' in filename or 'index-ar' in filename:
        replacements = [
            ('href="/tours.html"', 'href="/tours-ar.html"'),
            ('href="/blog.html"', 'href="/blog-ar.html"'),
            ('href="/index.html"', 'href="/ar/"'),
            ('href="tours.html"', 'href="tours-ar.html"'),
            ('href="blog.html"', 'href="blog-ar.html"'),
            ('href="index.html"', 'href="index-ar.html"'),
        ]
        
        for old, new in replacements:
            if old in fixed_content:
                fixed_content = fixed_content.replace(old, new)
    
    return fixed_content

def process_files():
    """
    Обрабатывает все HTML файлы.
    """
    # Находим все HTML файлы (исключая demo и output)
    html_files = glob.glob('/workspace/**/*.html', recursive=True)
    html_files = [f for f in html_files if 'demo' not in f and 'output' not in f and 'user_input' not in f]
    
    print("=" * 70)
    print("Исправление файлов")
    print("=" * 70)
    
    total_village_fixes = 0
    total_link_fixes = 0
    all_issues = []
    
    for file_path in sorted(html_files):
        filename = os.path.basename(file_path)
        rel_path = os.path.relpath(file_path, '/workspace')
        
        print(f"\nОбработка: {rel_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Исправляем название села
            new_content, village_changes = fix_village_name(content)
            if village_changes > 0:
                print(f"  ✓ Исправлено упоминаний села: {village_changes}")
                total_village_fixes += village_changes
                content = new_content
            
            # 2. Проверяем языковую логику
            issues = check_language_links(file_path, content)
            if issues:
                print(f"  ⚠️ Проблемы:")
                for issue in issues:
                    print(f"     - {issue}")
                    all_issues.append(f"{rel_path}: {issue}")
            
            # 3. Исправляем ссылки на языковые версии
            fixed_content = fix_language_links_in_content(content, filename)
            if fixed_content != content:
                print(f"  ✓ Исправлены ссылки на языковые версии")
                total_link_fixes += 1
                content = fixed_content
            
            # 4. Сохраняем изменения если были
            if village_changes > 0 or fixed_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Файл сохранён с исправлениями")
            else:
                print(f"  ✓ Файл проверен, изменений не требуется")
                
        except Exception as e:
            print(f"  ✗ Ошибка: {e}")
            all_issues.append(f"{rel_path}: Ошибка обработки - {e}")
    
    print("\n" + "=" * 70)
    print("ИТОГОВЫЙ ОТЧЁТ")
    print("=" * 70)
    print(f"Всего исправлено упоминаний села: {total_village_fixes}")
    print(f"Всего исправлено файлов со ссылками: {total_link_fixes}")
    print(f"Всего найдено проблем: {len(all_issues)}")
    
    if all_issues:
        print("\nСписок проблем для ручной проверки:")
        for issue in all_issues:
            print(f"  - {issue}")
    
    print("=" * 70)

if __name__ == '__main__':
    process_files()
