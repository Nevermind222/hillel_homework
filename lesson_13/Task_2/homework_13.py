import json
import logging
import os

logging.basicConfig(filename='json_savchyn.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validate_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in file {file_path}: {e}")


def validate_json_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            validate_json_file(file_path)


directory_path = r'..\Task_2'
validate_json_files_in_directory(directory_path)
