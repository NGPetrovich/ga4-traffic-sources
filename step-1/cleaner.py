import csv
import os

def extract_data_from_date(csv_file, output_file_name):
    # Define the output folder path relative to the current script location
    output_folder_path = "../step-2"
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Ensure the output folder exists, create if it does not
    os.makedirs(output_folder_path, exist_ok=True)

    found_date = False
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        with open(output_file_path, 'w', newline='') as output_csv:
            writer = csv.writer(output_csv)
            for row in reader:
                if found_date and not row[:3] == ['', '', '']:
                    writer.writerow(row)
                elif "Date" in row:
                    writer.writerow(row)
                    found_date = True
    if found_date:
        print(f'Extracted data from "Date" onwards to: {output_file_path}')
    else:
        print('Could not find "Date" in the CSV file')

if __name__ == "__main__":
    input_csv_file = input("Enter input CSV file name: ")
    extract_data_from_date(input_csv_file, "fake_clean.csv")
