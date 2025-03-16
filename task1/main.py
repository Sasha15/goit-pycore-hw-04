from pathlib import Path


def total_salary(path: str) -> tuple | str:
    path = Path(path)

    if path.is_file():
        try:
            with open(path, mode='r', encoding='utf-8', errors="strict") as f:
                lines = f.readlines()

                if len(lines) == 0:
                    return "File is empty"
                
                # Filter out empty lines
                lines = [line for line in lines if line.strip()]

                lines = [line.split(',')[1].rstrip() for line in lines]
                sum_salary = sum([int(salary) for salary in lines])
                avg_salary = round(sum_salary / len(lines))

                return (sum_salary, avg_salary)
        except Exception as e:
            return f"Error opening file: {e}"
    else:
        return "File not found"
    
    
total, average = total_salary('./task1/salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")