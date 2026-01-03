#!/usr/bin/env python3
"""
Скрипт для создания правильного Google Maps embed URL
с центром на Красной Слободе и спутниковым видом по умолчанию
"""

def create_map_embed_url(lat, lon, zoom=17):
    """
    Создаёт правильный URL для Google Maps embed со спутниковым видом.
    """
    # Для спутникового вида используем параметр &t=h (hybrid) или &maptype=satellite
    
    # Формат URL для Google Maps embed API
    embed_url = f'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3105.5!2d{lon}!3d{lat}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f{zoom}!3m3!1m2!1s0x0%3A0x0!2z{lat}N%2C%20{lon}E!5m2!1sru!2s'
    
    return embed_url

def fix_map_in_file():
    """
    Исправляет карту в файле blog-red-village-ru.html
    """
    file_path = '/workspace/blog-red-village-ru.html'
    
    # Координаты Красной Слободы
    lat = "41.37035015005354"
    lon = "48.51409202400067"
    zoom = "17"
    
    print("=" * 60)
    print("Исправление карты Google Maps")
    print("=" * 60)
    print(f"Координаты: {lat}°N, {lon}°E")
    print(f"Zoom: {zoom}z")
    print("Режим: Спутниковый (Hybrid)")
    print()
    
    # Читаем файл
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Создаём правильный URL для спутникового вида
    # Для гибридного вида (спутник + дороги) используем параметр t=h
    new_url = f'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3105.5!2d{lon}!3d{lat}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f{zoom}!3m3!1m2!1s0x0%3A0x0!2z{lat}N%2C%20{lon}E!5m2!1sru!2s&t=h&z={zoom}'
    
    # Находим iframe с картой
    # Паттерн для поиска существующего iframe
    import re
    
    # Ищем iframe с Google Maps
    iframe_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed\?pb[^"]*"[^>]*></iframe>'
    
    match = re.search(iframe_pattern, content, re.DOTALL)
    
    if match:
        old_iframe = match.group()
        print(f"Найден старый iframe карты")
        
        # Создаём новый iframe с правильным URL
        new_iframe = f'''<iframe 
          width="100%" 
          height="450" 
          frameborder="0" 
          style="border:0; border-radius: 16px;"
          src="{new_url}"
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade"
          title="Красная Слобода - спутниковый вид Google Maps">
        </iframe>'''
        
        # Заменяем старый iframe
        content = content.replace(old_iframe, new_iframe)
        
        # Также обновляем подзаголовок
        old_subtitle = 'Координаты: 41.3635°N, 48.5180°E | Интерактивный спутниковый вид'
        new_subtitle = f'Координаты: {lat}°N, {lon}°E | Спутниковый вид (Красная Слобода)'
        content = content.replace(old_subtitle, new_subtitle)
        
        print("✓ Создан новый iframe с правильными параметрами")
        print(f"✓ Обновлён подзаголовок карты")
        
        # Сохраняем файл
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print()
        print("=" * 60)
        print("Файл сохранён!")
        print("=" * 60)
        
        # Выводим URL для проверки
        print("\nНовый URL карты:")
        print(new_url)
        
    else:
        print("✗ Не найден iframe с картой Google Maps")

if __name__ == '__main__':
    fix_map_in_file()
