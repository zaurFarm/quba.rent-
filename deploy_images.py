#!/usr/bin/env python3
"""
Скрипт для загрузки изображений на сервер через FTP
"""

from ftplib import FTP
import os

def deploy_images():
    """Загрузка изображений на FTP-сервер"""
    
    # Параметры подключения
    host = '95.216.232.219'
    port = 19121
    username = 'www-data'
    password = '0R6dXU1YnwSEl1OnURos'
    
    # Список изображений для загрузки
    images_to_upload = [
        '/workspace/images/blog-red-village-authentic1.jpg',
        '/workspace/images/blog-red-village-authentic2.jpg', 
        '/workspace/images/blog-red-village-authentic3.jpg',
    ]
    
    print("=" * 60)
    print("Загрузка изображений на сервер")
    print("=" * 60)
    
    try:
        # Подключение к серверу
        print(f"Подключение к {host}:{port}...")
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print("Подключение успешно!")
        
        # Создаём папку images если её нет
        try:
            ftp.mkd('images')
            print("Создана папка 'images'")
        except:
            print("Папка 'images' уже существует")
        
        uploaded_count = 0
        error_count = 0
        
        for image_path in images_to_upload:
            if not os.path.exists(image_path):
                print(f"  ⚠ Файл не найден: {image_path}")
                continue
                
            filename = os.path.basename(image_path)
            remote_path = f'images/{filename}'
            print(f"\\nЗагрузка: {filename} в папку images...")
            
            try:
                # Удаляем старый файл
                try:
                    ftp.delete(remote_path)
                except:
                    pass
                
                # Загружаем новый файл в папку images
                with open(image_path, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_path}', f)
                
                print(f"  ✓ {filename} загружен в images/ успешно!")
                uploaded_count += 1
                
            except Exception as e:
                print(f"  ✗ Ошибка при загрузке {filename}: {e}")
                error_count += 1
        
        # Закрываем соединение
        ftp.quit()
        print("\\nСоединение закрыто.")
        
        print("\\n" + "=" * 60)
        print(f"Загрузка завершена!")
        print(f"Успешно загружено: {uploaded_count}")
        print(f"Ошибок: {error_count}")
        print("=" * 60)
        
    except Exception as e:
        print(f"Ошибка при подключении: {e}")

if __name__ == '__main__':
    deploy_images()
