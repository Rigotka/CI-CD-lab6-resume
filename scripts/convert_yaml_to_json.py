import yaml
import json
import os

def convert_yaml_to_json(yaml_file_path, json_file_path):
    with open(yaml_file_path, 'r', encoding='utf-8') as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    yaml_file_path = 'src/resume.yaml'
    json_file_path = 'src/resume.json'

    convert_yaml_to_json(yaml_file_path, json_file_path)
    print(f"JSON file created at {json_file_path}")