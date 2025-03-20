import os
import pandas as pd


def collect_file_names(root_dir):
    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            file_paths.append(full_path)
    return file_paths


def save_to_excel(file_paths, output_file):
    df = pd.DataFrame(file_paths, columns=["File Path"])
    df.to_excel(output_file, index=False)
    print(f"File paths saved to {output_file}")


def main():
    root_dir = input("Enter the root directory path: ")
    output_file = input("Enter the output Excel file name (e.g., output.xlsx): ")+'.xlsx'
    file_paths = collect_file_names(root_dir)
    save_to_excel(file_paths, output_file)


if __name__ == "__main__":
    main()