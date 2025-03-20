import pandas as pd

def csv_to_json(csv_file, json_file):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to JSON and save to a file
    df.to_json(json_file, orient='records', lines=True)

    print(f"CSV file {csv_file} has been converted to JSON and saved as {json_file}")

def main():
    # Get file paths from the user
    csv_file = input("Enter the CSV file path: ")
    json_file = input("Enter the output JSON file name (e.g., output.json): ")

    # Call the conversion function
    csv_to_json(csv_file, json_file)

if __name__ == "__main__":
    main()
