import os
import sys
from pathlib import Path

def count_files_and_folders(directory_path):
    """
    Подсчитывает количество файлов и папок в указанной директории
    """
    try:
        # Преобразуем путь в Path объект
        path = Path(directory_path)
        
        # Проверяем существование директории
        if not path.exists():
            print(f"Ошибка: Директория '{directory_path}' не существует!")
            return
        
        if not path.is_dir():
            print(f"Ошибка: '{directory_path}' не является директорией!")
            return
        
        # Получаем список всех элементов в директории
        items = list(path.iterdir())
        
        # Подсчитываем файлы и папки
        files_count = 0
        folders_count = 0
        
        for item in items:
            if item.is_file():
                files_count += 1
            elif item.is_dir():
                folders_count += 1
        
        # Выводим результаты
        print(f"\nРезультаты для директории: {directory_path}")
        print(f"📁 Папок: {folders_count}")
        print(f"📄 Файлов: {files_count}")
        print(f"📊 Всего элементов: {len(items)}")
        
    except PermissionError:
        print(f"Ошибка: Нет прав доступа к директории '{directory_path}'")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    """
    Основная функция скрипта
    """
    print("🔍 Скрипт для подсчета файлов и папок в директории")
    print("-" * 50)
    
    # Получаем путь от пользователя
    if len(sys.argv) > 1:
        # Если путь передан как аргумент командной строки
        directory_path = sys.argv[1]
    else:
        # Запрашиваем путь у пользователя
        directory_path = input("Введите путь к директории: ").strip()
    
    # Если путь пустой, используем текущую директорию
    if not directory_path:
        directory_path = "."
        print("Используется текущая директория")
    
    # Вызываем функцию подсчета
    count_files_and_folders(directory_path)

if __name__ == "__main__":
    main()