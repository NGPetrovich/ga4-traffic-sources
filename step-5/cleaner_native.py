import csv
import os
import re

def header_matches(row, header_keywords_list):
    # Flatten the row to a single string for matching, with whitespace normalized
    row_string = ' '.join(cell.strip() for cell in row if cell.strip())
    row_string = re.sub(' +', ' ', row_string)
    # Check for the presence of all header keywords in the row string
    return all(re.search(r'\b' + re.escape(keyword) + r'\b', row_string, re.IGNORECASE) for keyword in header_keywords_list)

def extract_data_from_header(csv_file, output_file_name, header_keywords):
    output_folder_path = "../step-6"
    output_file_path = os.path.join(output_folder_path, output_file_name)
    os.makedirs(output_folder_path, exist_ok=True)

    header_keywords_list = header_keywords.split()

    found_header = False
    skip_next_row = False
    with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        with open(output_file_path, 'w', newline='', encoding='utf-8') as output_csv:
            writer = csv.writer(output_csv)
            for row in reader:
                # Skip empty rows and rows after the header
                if skip_next_row or not any(cell.strip() for cell in row):
                    skip_next_row = False
                    continue
                if found_header:
                    writer.writerow(row)
                elif header_matches(row, header_keywords_list):
                    writer.writerow(row)  # Write the original header row
                    found_header = True
                    skip_next_row = True  # Skip the next row as it's just after the header

    if found_header:
        print(f'Extracted data starting from header "{header_keywords}" to: {output_file_path}')
    else:
        print(f'Could not find header "{header_keywords}" in the CSV file')

if __name__ == "__main__":
    input_csv_file = input("Enter input CSV file name: ")
    header_keywords = "FTD Attempted NATIVE User ID"
    extract_data_from_header(input_csv_file, "clean_native_data.csv", header_keywords)
