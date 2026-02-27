import os
from config.settings import SUPPORTED_EXTENSIONS, IGNORE_DIRS

def read_codebase(root_path):
    
    files_data = []
    
    for root, dirs, files in os.walk(root_path):
    
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
    
        for file in files:
    
            ext = os.path.splitext(file)[1]
    
            if ext in SUPPORTED_EXTENSIONS:
    
                file_path = os.path.join(root, file)
    
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        files_data.append({
                            "path": file_path,
                            "content": content
                        })
                except Exception as e:
                    print("Error reading", file_path)
    
    return files_data