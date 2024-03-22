import yaml

def save_yaml(filepath, content):
        with open(filepath, "w", encoding="utf-8") as file:
            yaml.dump(content, file, allow_unicode=True)

def save_file(filepath, content):
        with open(filepath, "w", encoding="utf-8") as outfile:
            outfile.write(content)

def open_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()
    except:
        return None
