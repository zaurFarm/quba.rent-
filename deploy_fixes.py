#!/usr/bin/env python3
"""
Скрипт для загрузки обновлённых файлов на сервер через FTP
"""

from ftplib import FTP
import os

def deploy_updated_files():
    """Загрузка обновлённых файлов на FTP-сервер"""
    
    # Параметры подключения
    host = '95.216.232.219'
    port = 19121
    username = 'www-data'
    password = '0R6dXU1YnwSEl1OnURos'
    
    # Список файлов для загрузки
    files_to_upload = [
        ('/workspace/blog-red-village-ru.html', 'blog-red-village-ru.html'),
        ('/workspace/quba.rent/index-ru.html', 'index-ru.html'),
        ('/workspace/images/blog-red-village-authentic1.jpg', 'images/blog-red-village-authentic1.jpg'),
        ('/workspace/images/blog-red-village-authentic2.jpg', 'images/blog-red-village-authentic2.jpg'),
        ('/workspace/images/blog-red-village-authentic3.jpg', 'images/blog-red-village-authentic3.jpg'),
    ]
    
    print("=" * 60)
    print("Загрузка обновлённых файлов на сервер")
    print("=" * 60)
    
    try:
        # Подключение к серверу
        print(f"Подключение к {host}:{port}...")
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print("Подключение успешно!")
        
        uploaded_count = 0
        error_count = 0
        
        for local_path, remote_path in files_to_upload:
            if not os.path.exists(local_path):
                print(f"  ⚠ Файл не найден: {local_path}")
                continue
                
            print(f"\nЗагрузка: {remote_path}...")
            
            try:
                # Создаём папку если нужно
                remote_dir = os.path.dirname(remote_path)
                if remote_dir and remote_dir != '.':
                    try:
                        ftp.mkd(remote_dir)
                    except:
                        pass  # Папка уже существует
                
                # Удаляем старый файл
                try:
                    ftp.delete(remote_path)
                except:
                    pass
                
                # Загружаем новый файл
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_path}', f)
                
                print(f"  ✓ {remote_path} загружен успешно!")
                uploaded_count += 1
                
            except Exception as e:
                print(f"  ✗ Ошибка при загрузке {remote_path}: {e}")
                error_count += 1
        
        # Закрываем соединение
        ftp.quit()
        print("\nСоединение закрыто.")
        
        print("\n" + "=" * 60)
        print(f"Загрузка завершена!")
        print(f"Успешно загружено: {uploaded_count}")
        print(f"Ошибок: {error_count}")
        print("=" * 60)
        
    except Exception as e:
        print(f"Ошибка при подключении: {e}")

if __name__ == '__main__':
    deploy_updated_files()
