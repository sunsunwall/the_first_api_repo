import json
from rich import print_json
from rich.console import Console
import sys


def main():
    filename = "smhi_data.json"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            data = f.read()
        console = Console()
        console.rule(f"[bold green]Contents of {filename}")
        print_json(data)
    except Exception as e:
        print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    main()
