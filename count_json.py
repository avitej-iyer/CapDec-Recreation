import json
import sys

def count_json_entries(file_path):
    """
    Counts the number of entries in a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        int: Number of entries in the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return len(data)
            elif isinstance(data, dict):
                return len(data.keys())
            else:
                print("Unsupported JSON format. Must be a list or a dictionary.")
                return 0
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except json.JSONDecodeError:
        print(f"Invalid JSON file: {file_path}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_json_entries.py <path_to_json_file>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    count = count_json_entries(json_file_path)
    print(f"Number of entries: {count}")
