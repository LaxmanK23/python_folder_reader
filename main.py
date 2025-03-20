import os
import pandas as pd

def collect_file_names(root_dir):
    file_info = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            file_info.append((full_path, file))  # Include both full path and file name
    return file_info

def save_to_excel(file_info, output_file):
    df = pd.DataFrame(file_info, columns=["File Path", "File Name"])  # Add file name column
    df.to_excel(output_file, index=False)
    print(f"File paths and names saved to {output_file}")

def main():
    root_dir = input("Enter the root directory path: ")
    output_file = input("Enter the output Excel file name (e.g., output.xlsx): ") + '.xlsx'
    file_info = collect_file_names(root_dir)
    save_to_excel(file_info, output_file)

if __name__ == "__main__":
    main()
