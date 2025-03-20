import os
import pandas as pd
import json

def read_json(json_file):
    """Read the JSON file and return the data."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def read_excel(excel_file):
    """Read the Excel file and return the data."""
    df = pd.read_excel(excel_file)
    print("Excel Columns: ", df.columns)  # Print the columns to help debug
    return df

def match_and_append_path(excel_data, json_data):
    """Match certificate names from JSON with the Excel data and append the file path."""
    # Create a dictionary with 'File Name' as key and 'File Path' as value from Excel data
    excel_dict = dict(zip(excel_data['File Name'], excel_data['File Path']))

    # Debugging: Print out a few sample names from both JSON and Excel
    print("Sample JSON names: ", [entry['name'] for entry in json_data][:5])
    print("Sample Excel file names: ", excel_data['File Name'].head())

    # Add a new field in JSON to store the matched file path
    for entry in json_data:
        name = entry.get('name', '')  # Use .get to avoid KeyError in case 'name' is missing
        if name in excel_dict:
            entry['filePath'] = excel_dict[name]
        else:
            entry['filePath'] = None  # If no match is found, set filePath to None

    return json_data

def save_to_excel(data, output_file):
    """Save the updated data to Excel with .xlsx format."""
    if not output_file.endswith('.xlsx'):
        output_file += '.xlsx'  # Append .xlsx if it's not already in the filename

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

def main():
    # Get the input file paths from the user
    json_file = input("Enter the JSON file path: ")
    excel_file = input("Enter the Excel file path: ")
    output_file = input("Enter the output Excel file name (e.g., output.xlsx): ")

    # Read the files
    json_data = read_json(json_file)
    excel_data = read_excel(excel_file)

    # Match certificate names and append the file path
    updated_json_data = match_and_append_path(excel_data, json_data)

    # Save the updated data to Excel
    save_to_excel(updated_json_data, output_file)

if __name__ == "__main__":
    main()
