import zipfile
import os

def extract_zip(zip_path, extract_to=None):
    if not zipfile.is_zipfile(zip_path):
        print("The file is not a valid zip archive.")
        return

    if extract_to is None:
        extract_to = os.path.splitext(zip_path)[0]  # Folder with the same name as the zip file

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted '{zip_path}' to '{extract_to}'")

# Example usage
zip_file_path = 'day-61-starting-files-flask-secrets.zip'  # Replace with your zip file path
extract_zip(zip_file_path)
