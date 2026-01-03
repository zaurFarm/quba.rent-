#!/usr/bin/env python3
"""
Скрипт для обновления стилей в blog-red-village-ru.html:
1. Замена фона .cta-section на SVG-паттерн
2. Удаление красного оверлея в шапке
"""

import re

def read_file(filepath):
    """Чтение файла"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Запись файла"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Файл обновлён: {filepath}")

def encode_svg_for_css(svg_content):
    """
    Преобразование SVG-контента в URL-совместимый формат для CSS.
    """
    # Удаляем XML-прокомментировать и переносы строк
    svg_clean = re.sub(r'<!--.*?-->', '', svg_content, flags=re.DOTALL)
    svg_clean = re.sub(r'\s+', ' ', svg_clean)
    svg_clean = svg_clean.strip()
    
    # URL-encode специальные символы для CSS data URI
    # Порядок важен - сначала более длинные замены
    replacements = [
        ('"', '%22'),
        ("'", "%27"),
        ('#', '%23'),
        ('{', '%7B'),
        ('}', '%7D'),
        ('<', '%3C'),
        ('>', '%3E'),
        ('[', '%5B'),
        (']', '%5D'),
        (' ', '%20'),
    ]
    
    for old, new in replacements:
        svg_clean = svg_clean.replace(old, new)
    
    return svg_clean

def update_cta_section(content, svg_encoded):
    """
    Обновление стилей для .cta-section - добавление SVG-фона.
    """
    # Новый стиль для .cta-section с SVG-фоном
    new_cta_styles = '''.cta-section {{
      background: url("data:image/svg+xml,{svg_encoded}"), linear-gradient(135deg, #2F5233 0%, #1a3d1f 100%);
      color: white;
      padding: 60px 20px;
      text-align: center;
      margin: 60px 0;
      border-radius: 16px;
      position: relative;
      overflow: hidden;
    }}
    .cta-section::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(47, 82, 51, 0.7);
      pointer-events: none;
    }}
    .cta-section h3, .cta-section p, .cta-section a {{
      position: relative;
      z-index: 1;
    }}'''.format(svg_encoded=svg_encoded)
    
    # Паттерн для поиска старых стилей .cta-section
    cta_pattern = r'\.cta-section \{[^}}]+\}'
    
    # Заменяем стили
    content = re.sub(cta_pattern, new_cta_styles, content, flags=re.DOTALL)
    
    print("Стили .cta-section обновлены с SVG-фоном")
    return content

def update_hero_overlay(content):
    """
    Обновление .hero-overlay - удаление красного оттенка.
    Заменяем красный градиент на нейтральный тёмный.
    """
    # Заменяем красный градиент на нейтральный
    old_overlay = '''.hero-overlay {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(to bottom, rgba(139, 0, 0, 0.6), rgba(139, 0, 0, 0.85));
    }'''
    
    new_overlay = '''.hero-overlay {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(to bottom, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6));
    }'''
    
    content = content.replace(old_overlay, new_overlay)
    
    print("Оверлей в шапке обновлён - красный оттенок удалён")
    return content

def main():
    # Пути к файлам
    html_file = '/workspace/blog-red-village-ru.html'
    svg_file = '/workspace/imgs/n_guba.svg'
    
    print("=" * 60)
    print("Обновление стилей в blog-red-village-ru.html")
    print("=" * 60)
    
    # Читаем SVG файл
    print(f"Чтение SVG файла: {svg_file}")
    with open(svg_file, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Кодируем SVG для CSS
    print("Кодирование SVG для CSS...")
    svg_encoded = encode_svg_for_css(svg_content)
    print(f"SVG закодирован, длина: {len(svg_encoded)} символов")
    
    # Читаем HTML файл
    print(f"Чтение HTML файла: {html_file}")
    content = read_file(html_file)
    
    # Обновляем стили CTA секции
    print("\nОбновление стилей .cta-section...")
    content = update_cta_section(content, svg_encoded)
    
    # Обновляем оверлей в шапке
    print("Обновление оверлея в шапке...")
    content = update_hero_overlay(content)
    
    # Записываем результат
    write_file(html_file, content)
    
    print("\n" + "=" * 60)
    print("Обновление завершено успешно!")
    print("=" * 60)

if __name__ == '__main__':
    main()
