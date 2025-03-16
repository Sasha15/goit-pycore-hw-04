from pathlib import Path
import sys
from colorama import Fore, Style, init

""" 
Path can be relative with ../ or ../.. 
depeding on the location of the folder where the script is run
("python main.py ../folder" or "python main.py ../../folder" etc.)
"""
def main(directory: Path):
    
    if not directory.is_dir():
        print(Fore.RED + f"Error: '{directory}' is not a valid directory.")
        return

    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.BLUE + "📁 " + item.name)
        else:
            print("\t" + Fore.GREEN + "📝 " + item.name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python main.py <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1]).resolve()

    if not directory_path.exists():
        print(Fore.RED + f"Error: Path '{directory_path}' does not exist.")
        sys.exit(1)
    main(directory_path)