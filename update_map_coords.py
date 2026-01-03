#!/usr/bin/env python3
"""
Скрипт для обновления координат карты Красной Слободы
"""

def update_coordinates():
    """
    Обновляет координаты Google Maps в файле blog-red-village-ru.html
    """
    file_path = '/workspace/blog-red-village-ru.html'
    
    # Новые координаты
    new_lat = "41.37035015005354"
    new_lon = "48.51409202400067"
    
    print("=" * 60)
    print("Обновление координат карты Красной Слободы")
    print("=" * 60)
    print(f"Новые координаты: {new_lat}°N, {new_lon}°E")
    print()
    
    # Читаем файл
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    total_changes = 0
    
    # 1. Обновляем текст с координатами в подзаголовке
    old_coords_text = "Координаты: 41.3635°N, 48.5180°E"
    new_coords_text = f"Координаты: {new_lat}°N, {new_lon}°E"
    
    if old_coords_text in content:
        content = content.replace(old_coords_text, new_coords_text)
        total_changes += 1
        print(f"✓ Обновлён текст с координатами в подзаголовке")
    
    # 2. Обновляем координаты в URL Google Maps
    # Паттерны для замены
    patterns = [
        ('!2d48.518!3d41.3635', f'!2d{new_lon}!3d{new_lat}'),
        ('!3d41.3635!2d48.518', f'!3d{new_lat}!2d{new_lon}'),
        ('!2d48.518', f'!2d{new_lon}'),
        ('!3d41.3635', f'!3d{new_lat}'),
    ]
    
    for old_pat, new_pat in patterns:
        if old_pat in content:
            count = content.count(old_pat)
            content = content.replace(old_pat, new_pat)
            total_changes += count
            print(f"✓ Заменено '{old_pat}' -> '{new_pat}' ({count} раз)")
    
    # Сохраняем файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()
    print("=" * 60)
    print(f"Всего внесено изменений: {total_changes}")
    print(f"Файл сохранён: {file_path}")
    print("=" * 60)
    
    # Проверяем результат
    print("\nПроверка - поиск новых координат в файле:")
    if new_lat[:8] in content:
        print(f"✓ Координаты {new_lat[:8]}... найдены в файле")
    if new_lon[:8] in content:
        print(f"✓ Координаты {new_lon[:8]}... найдены в файле")

if __name__ == '__main__':
    update_coordinates()
