import pandas as pd
import glob

# File paths from glob search for csv and xlsx files
csv_files = glob.glob('*.csv')
excel_files = glob.glob('*.xlsx')

if not csv_files or not excel_files:
    raise FileNotFoundError("Could not find the required CSV and/or Excel files in the current directory.")

csv_filepath = csv_files[0]
excel_filepath = excel_files[0]
output_filepath = '../step-7/output.xlsx'  # Output file path

# Load the CSV and Excel files
csv_data = pd.read_csv(csv_filepath)
excel_data = pd.read_excel(excel_filepath)

# If the CSV data contains an 'Event value', rename it to avoid confusion
if 'Event value' in csv_data.columns:
    csv_data.rename(columns={'Event value': 'CSV Event value'}, inplace=True)

# Merge the datasets on the specified keys with a left join
merged_data = pd.merge(excel_data, csv_data, how='left',
                       left_on='Playercode', right_on='FTD Attempted NATIVE User ID')

# Conditional updating of 'Campaign' and 'Source/Medium' based on the presence of match
merged_data['Campaign'] = merged_data.apply(lambda x: x['Device brand'] if pd.notna(x['Device brand']) else x['Campaign'], axis=1)
merged_data['Source/Medium'] = merged_data.apply(lambda x: x['Operating system'] if pd.notna(x['Operating system']) else x['Source/Medium'], axis=1)

# Drop the original 'Device brand', 'Operating system', and any renamed 'CSV Event value'
columns_to_drop = ['Device brand', 'Operating system']
if 'CSV Event value' in merged_data.columns:
    columns_to_drop.append('CSV Event value')
merged_data.drop(columns=columns_to_drop, inplace=True)

# Save the resulting dataframe to a new Excel file
merged_data.to_excel(output_filepath, index=False)
print("Merged file saved to:", output_filepath)
