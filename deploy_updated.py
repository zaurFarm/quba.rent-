#!/usr/bin/env python3
"""
Скрипт для загрузки обновлённого файла на сервер через FTP
"""

from ftplib import FTP
import os

def deploy_to_server():
    """Загрузка файла на FTP-сервер"""
    
    # Параметры подключения
    host = '95.216.232.219'
    port = 19121
    username = 'www-data'
    password = '0R6dXU1YnwSEl1OnURos'
    
    local_file = '/workspace/blog-red-village-ru.html'
    remote_file = 'blog-red-village-ru.html'
    
    print("=" * 60)
    print("Загрузка файла на сервер")
    print("=" * 60)
    
    try:
        # Подключение к серверу
        print(f"Подключение к {host}:{port}...")
        ftp = FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print("Подключение успешно!")
        
        # Удаляем старый файл
        print(f"Удаление старого файла {remote_file}...")
        try:
            ftp.delete(remote_file)
            print("Старый файл удалён")
        except Exception as e:
            print(f"Файл для удаления не найден или ошибка: {e}")
        
        # Загружаем новый файл
        print(f"Загрузка {local_file}...")
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        print(f"Файл {remote_file} загружен успешно!")
        
        # Закрываем соединение
        ftp.quit()
        print("Соезакрыто.")
        
        print("\n" + "=" * 60)
        print("Загрузка завершена успешно!")
        print(f"Файл доступен по адресу: {remote_file}")
        print("=" * 60)
        
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

if __name__ == '__main__':
    deploy_to_server()
