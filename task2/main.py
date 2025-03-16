from pathlib import Path

def get_cats_info(path: str) -> list | str:
    path = Path(path)

    if not path.is_file():
        return "File not found"
    
    try:
        cats = []
        with open(path, mode='r', encoding='utf-8', errors="strict") as f:
            lines = f.readlines()

            if len(lines) == 0:
                return "File is empty"
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) < 3:
                    print(f"Invalid line format: {line}")
                    continue
                
                cats.append({"id": parts[0].strip(), "name": parts[1].strip(), "age": parts[2].strip()})
        if not cats:
            return "File is empty or contains no valid data"
        return cats
    except Exception as e:
        return f"Error reading file: {e}"
    
cats = get_cats_info('./task2/cats.txt')
print(cats)