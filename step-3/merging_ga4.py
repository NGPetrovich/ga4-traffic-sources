import pandas as pd
import glob

def auto_detect_and_merge_csv_files():
    # Find all CSV files in the current directory
    csv_files = glob.glob('*.csv')
    if len(csv_files) != 2:
        raise ValueError("There should be exactly two CSV files in the directory.")
    
    # Load the CSV files
    df1 = pd.read_csv(csv_files[0])
    df2 = pd.read_csv(csv_files[1])
    
    # Determine the primary and secondary dataframes based on the number of columns
    if df1.shape[1] < df2.shape[1]:
        primary_df, secondary_df = df1, df2
        primary_file, secondary_file = csv_files[0], csv_files[1]
    else:
        primary_df, secondary_df = df2, df1
        primary_file, secondary_file = csv_files[1], csv_files[0]

    print(f"Primary file: {primary_file}, Secondary file: {secondary_file}")
    
    # Identify the key columns - assuming they are named consistently as 'Playercode' and 'FTD Attempted User ID'
    # If the columns are named differently, you may need to adjust this logic
    if 'Playercode' in primary_df.columns and 'FTD Attempted User ID' in secondary_df.columns:
        # Ensure key columns in both dataframes have the same data type (int)
        primary_df['Playercode'] = primary_df['Playercode'].astype('int')
        secondary_df['FTD Attempted User ID'] = secondary_df['FTD Attempted User ID'].astype('int')

        # Merge the dataframes
        merged_df = pd.merge(primary_df, secondary_df, left_on='Playercode', right_on='FTD Attempted User ID', how='left')
        
        # Optional: Clean up the dataframe as needed before saving
        # For instance, dropping the 'FTD Attempted User ID' column if it's no longer needed
        merged_df.drop('FTD Attempted User ID', axis=1, inplace=True)
        
        # Save the merged dataframe to an Excel file
        output_excel_path = '../step-4/merged_data.xlsx'
        merged_df.to_excel(output_excel_path, index=False)
        print(f"Merged data saved to {output_excel_path}.")
    else:
        print("The necessary key columns ('Playercode' and 'FTD Attempted User ID') were not found in the dataframes.")

if __name__ == "__main__":
    auto_detect_and_merge_csv_files()
