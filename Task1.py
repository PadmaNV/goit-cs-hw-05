import asyncio
import os
import shutil
import logging
from argparse import ArgumentParser
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

def parse_arguments():
    parser = ArgumentParser(description="Розподіл файлів з вихідної папки у цільову папку за розширенням")
    parser.add_argument("source_folder", help="Шлях до вихідної папки")
    parser.add_argument("output_folder", help="Шлях до цільової папки")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    source_folder = args.source_folder
    output_folder = args.output_folder

    logging.basicConfig(level=logging.INFO)

    if not os.path.isdir(source_folder):
        print("Вихідна папка не існує.")
        exit()

    asyncio.run(read_folder(source_folder, output_folder))

