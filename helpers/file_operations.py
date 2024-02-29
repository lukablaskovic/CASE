import os
import pandas as pd

def normalize_line_endings(s):
    """
    Normalize the line endings in a string to Unix-like (\n), without altering
    escape sequences within string literals.
    
    :param s: The string with potential mixed line endings (\r\n, \r, \n).
    :return: A string with normalized line endings (\n).
    """
    return s.replace('\r\n', '\n').replace('\r', '\n')


def export_dict_to_csv(data, file_path):
    """
    Exports a dictionary or a list of dictionaries to a CSV file using pandas.

    Parameters:
    - data: A dictionary or a list of dictionaries to be exported.
    - file_path: The file path (including file name) where the CSV will be saved.

    Returns:
    - None
    """
    assert isinstance(data, (dict, list)), "Data must be a dictionary or a list of dictionaries."
    if isinstance(data, list):
        assert all(isinstance(item, dict) for item in data), "All items in the list must be dictionaries."

    df = pd.DataFrame(data if isinstance(data, list) else [data])

    # Export the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"Data successfully written to {file_path}")

def find_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while current_dir != os.path.dirname(current_dir):
        if "config.py" in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

def read_file_content(filename):
    project_root = find_project_root()
    if not project_root:
        return "Error: Project root could not be determined."

    file_path = os.path.join(project_root, filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found in the project root."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"