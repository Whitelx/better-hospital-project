import json
import os

def load_json(file_path):
    
    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
        
    except json.JSONDecodeError:
        
        return []
    

def save_json(file_path, data):
    
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)