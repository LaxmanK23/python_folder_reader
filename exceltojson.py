import pandas as pd
import json

def excel_to_json(excel_file, json_file):
    # Read Excel file into a DataFrame
    df = pd.read_excel(excel_file)

    # Convert DataFrame to JSON format as an array of objects
    json_data = df.to_dict(orient='records')

    # Write the JSON data into a file with square brackets and commas separating the objects
    with open(json_file, 'w') as json_file_out:
        json.dump(json_data, json_file_out, indent=4)

    print(f"Excel file {excel_file} has been converted to JSON and saved as {json_file}")

def main():
    # Get file paths from the user
    excel_file = input("Enter the Excel file path: ")
    json_file = input("Enter the output JSON file name (e.g., output.json): ")

    # Call the conversion function
    excel_to_json(excel_file, json_file)

if __name__ == "__main__":
    main()
