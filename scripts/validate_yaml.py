import yaml

def validate_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print("YAML file is valid.")
    except yaml.YAMLError as exc:
        print(f"Error in YAML file: {exc}")

if __name__ == "__main__":
    validate_yaml('src/resume.yaml')