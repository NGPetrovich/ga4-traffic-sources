import csv

def extract_data_from_date(csv_file, output_file):
    found_date = False
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        with open(output_file, 'w', newline='') as output_csv:
            writer = csv.writer(output_csv)
            for row in reader:
                if found_date and not row[:3] == ['', '', '']:
                    writer.writerow(row)
                elif "Date" in row:
                    writer.writerow(row)
                    found_date = True
    if found_date:
        print(f'Extracted data from "Date" onwards to: {output_file}')
    else:
        print('Could not find "Date" in the CSV file')

if __name__ == "__main__":
    input_csv_file = input("Enter input CSV file name: ")
    output_csv_file = input("Enter output CSV file name: ")

    extract_data_from_date(input_csv_file, output_csv_file)
