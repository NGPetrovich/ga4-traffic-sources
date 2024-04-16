import pandas as pd
import glob

# Directory where your files are located (change this to your directory)
directory_path = './'  # Using the current directory; adjust as needed

# Use glob to find the Excel and CSV files
excel_file_path = glob.glob(f'{directory_path}*.xlsx')[0]  # Takes the first .xlsx file found
csv_file_path = glob.glob(f'{directory_path}*.csv')[0]    # Takes the first .csv file found

# Load the Excel file
excel_data = pd.read_excel(excel_file_path)

# Define a custom order for "Source/Medium" that puts undesired values last
priority = {"(direct) / (none)": 2, "(not set)": 2}
excel_data['Priority'] = excel_data['Source/Medium'].map(priority).fillna(1)

# Sort by "Playercode" and "Priority"
excel_data.sort_values(by=['Playercode', 'Priority'], ascending=[True, True], inplace=True)

# Drop duplicates based on "Playercode" after sorting
excel_data = excel_data.drop_duplicates(subset=['Playercode'], keep='first')

# Remove columns which are not needed
excel_data = excel_data.drop(columns=['FTD Attempted NATIVE User ID'])
excel_data = excel_data.drop(columns=['Unnamed: 4'])

# Load the CSV file for mapping
csv_data = pd.read_csv(csv_file_path)

# Create a mapping dictionary from the CSV data
channel_mapping = dict(zip(csv_data['GA4 Channel Name'], csv_data['Channel Name']))

# Update the "Source/Medium" column in the Excel file based on the mapping
# If a match is not found, the original value is retained using `fillna`
excel_data['Source/Medium'] = excel_data['Source/Medium'].map(channel_mapping).fillna(excel_data['Source/Medium'])

# Remove the temporary priority column
excel_data.drop(columns=['Priority'], inplace=True)

# Specify the path where you want to save the updated Excel file
updated_excel_file_path = f'../final.xlsx'

# Save the updated Excel file
excel_data.to_excel(updated_excel_file_path, index=False)

print(f"Updated Excel file has been saved to: {updated_excel_file_path}")
