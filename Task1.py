import asyncio
import os
import shutil
import logging
from pathlib import Path

async def read_folder(source_folder, output_folder):
    for file_path in Path(source_folder).rglob('*'):
        if file_path.is_file():
            await copy_file(file_path, output_folder)

async def copy_file(file_path, output_folder):
    extension = file_path.suffix[1:]  # Отримання розширення файлу без крапки
    destination_folder = os.path.join(output_folder, extension)
    os.makedirs(destination_folder, exist_ok=True)
    try:
        shutil.copy(file_path, destination_folder)
        logging.info(f"Скопійовано {file_path} до {destination_folder}")
    except Exception as e:
        logging.error(f"Помилка копіювання {file_path}: {e}")

if __name__ == "__main__":
    source_folder = input("Введіть шлях до вихідної папки: ").strip()
    output_folder = input("Введіть шлях до цільової папки: ").strip()

    logging.basicConfig(level=logging.INFO)

    if not os.path.isdir(source_folder):
        print("Вихідна папка не існує.")
        exit()

    asyncio.run(read_folder(source_folder, output_folder))
