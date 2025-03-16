from pathlib import Path


def total_salary(path: str) -> tuple | str:
    path = Path(path)

    if not path.is_file():
        return "File not found"

    try:
        total, count = 0, 0

        with open(path, mode='r', encoding='utf-8', errors="strict") as f:
            lines = f.readlines()

            if len(lines) == 0:
                return "File is empty"

            for line in lines:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(',')
                if len(parts) < 2:
                    return f"Invalid line format: {line}"
                
                try:
                    salary = int(parts[1].strip())
                    total += salary
                    count += 1
                except ValueError:
                    return f"Invalid salary value: {parts[1].strip()}"

            if count == 0:
                return "File is empty or contains no valid salaries"

            avg_salary = round(total / count)
            return (total, avg_salary)
    except Exception as e:
        return f"Error reading file: {e}"
    
    
total, average = total_salary('./task1/salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")