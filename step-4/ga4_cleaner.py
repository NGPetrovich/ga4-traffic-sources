import pandas as pd
import glob
import os

current_directory = os.getcwd()

files_in_directory = os.listdir(current_directory)

excel_files = [file for file in files_in_directory if file.endswith('.xlsx')]

if len(excel_files) == 1:
    excel_file_path = os.path.join(current_directory, excel_files[0])
    print("Excel file found:", excel_file_path)

    # Load the Excel file
    df = pd.read_excel(excel_file_path)

    # Apply the necessary transformations
    df['Date'] = df['Date'].fillna(df['First Deposit Date'])
    df['First user Google Ads keyword text'].fillna('(not set)', inplace=True)
    df['Campaign'].fillna('UNKNOWN', inplace=True)
    df['Source/Medium'].fillna('UNKNOWN', inplace=True)
    df['Total users'] = 1
    df['Event value'] = df['Total deposits']

    # Select and rename the required columns
    final_df = df[['Date', 'First user Google Ads keyword text', 'Campaign', 'Source/Medium', 'Playercode', 'Total users', 'Event value']]

    output_file_path = '../step-6/selected_data.xlsx'
    final_df.to_excel(output_file_path, index=False)

    print(f"Processed file saved as: {output_file_path}")
else:
    print("No Excel files found in the specified directory.")
