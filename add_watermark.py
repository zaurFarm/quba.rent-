#!/usr/bin/env python3
"""
Скрипт для добавления водяного знака с адресом сайта на все изображения статьи.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(image_path, output_path, text="www.Quba.rent"):
    """
    Добавление водяного знака на изображение.
    Водяной знак размещается в правом нижнем углу.
    """
    try:
        # Открываем изображение
        img = Image.open(image_path)
        
        # Конвертируем в RGB если нужно (для JPEG)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Создаём слой для рисования
        draw = ImageDraw.Draw(img)
        
        # Размеры изображения
        width, height = img.size
        
        # Размер текста пропорционально размеру изображения
        font_size = int(min(width, height) * 0.04)
        font_size = max(24, min(font_size, 72))  # Ограничиваем размер
        
        # Попытка загрузить шрифт (с запасом для разных систем)
        try:
            # Попробуем разные шрифты
            font_paths = [
                '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
                '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
                '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',
                '/System/Library/Fonts/Helvetica.ttc',  # macOS
                'C:\\Windows\\Fonts\\arial.ttf',  # Windows
            ]
            
            font = None
            for font_path in font_paths:
                if os.path.exists(font_path):
                    font = ImageFont.truetype(font_path, font_size)
                    break
            
            if font is None:
                font = ImageFont.load_default()
                
        except Exception as e:
            print(f"  Предупреждение: не удалось загрузить шрифт: {e}")
            font = ImageFont.load_default()
        
        # Получаем размер текста
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Позиция: правый нижний угол с отступом
        padding = int(min(width, height) * 0.03)
        x = width - text_width - padding
        y = height - text_height - padding
        
        # Создаём полупрозрачную подложку
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Размер подложки немного больше текста
        box_padding = int(font_size * 0.5)
        box_x1 = x - box_padding
        box_y1 = y - box_padding
        box_x2 = x + text_width + box_padding
        box_y2 = y + text_height + box_padding
        
        # Рисуем подложку с градиентом (полупрозрачный чёрный)
        overlay_draw.rectangle(
            [box_x1, box_y1, box_x2, box_y2],
            fill=(0, 0, 0, 128)
        )
        
        # Наложение на оригинальное изображение
        img = Image.alpha_composite(img.convert('RGBA'), overlay)
        draw = ImageDraw.Draw(img)
        
        # Рисуем текст белым цветом с лёгкой тенью
        # Тень
        draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0, 180))
        # Основной текст
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))
        
        # Конвертируем обратно и сохраняем
        img = img.convert('RGB')
        img.save(output_path, 'JPEG', quality=95)
        
        print(f"  ✓ Обработано: {os.path.basename(image_path)}")
        return True
        
    except Exception as e:
        print(f"  ✗ Ошибка при обработке {image_path}: {e}")
        return False

def process_all_images():
    """
    Обработка всех изображений из статьи.
    """
    # Список изображений, используемых в статье blog-red-village-ru.html
    images_to_process = [
        '/workspace/images/blog-red-village-authentic1.jpg',
        '/workspace/images/blog-red-village-authentic2.jpg', 
        '/workspace/images/blog-red-village-authentic3.jpg',
    ]
    
    watermark_text = "www.Quba.rent"
    
    print("=" * 60)
    print("Добавление водяного знака на изображения статьи")
    print(f"Текст водяного знака: {watermark_text}")
    print("=" * 60)
    
    processed_count = 0
    error_count = 0
    
    for image_path in images_to_process:
        
        # Проверяем существование файла
        if not os.path.exists(image_path):
            print(f"  ⚠ Файл не найден: {image_path}")
            continue
        
        print(f"\nОбработка: {image_path}")
        
        # Добавляем водяной знак
        if add_watermark(image_path, image_path, watermark_text):
            processed_count += 1
        else:
            error_count += 1
    
    print("\n" + "=" * 60)
    print(f"Обработка завершена!")
    print(f"Успешно обработано: {processed_count}")
    print(f"Ошибок: {error_count}")
    print("=" * 60)
    
    return processed_count > 0

if __name__ == '__main__':
    process_all_images()
