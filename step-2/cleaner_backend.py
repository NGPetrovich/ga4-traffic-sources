import pandas as pd
import glob

# Find all Excel files in the current directory
excel_files = glob.glob('*.xlsx')

if not excel_files:
    print("No Excel files found in the directory.")
else:
    # Use the first Excel file found
    file_name = excel_files[0]
    df = pd.read_excel(file_name, header=2)  # Headers are on the third row

    # Convert 'First Deposit Date' to datetime format for filtering
    df['First Deposit Date'] = pd.to_datetime(df['First Deposit Date'], errors='coerce')

    # Function to filter data based on user input and save to CSV
    def filter_data_by_date_and_save(df):
        # User inputs for month and year
        month_name = input("Data from which month would you like to see? ").strip().capitalize()
        year = input("Data from which year would you like to see? ").strip()

        try:
            # Convert month name to month number
            month_num = pd.to_datetime(month_name, format='%B').month
            year = int(year)  # Ensure year is an integer

            # Filter DataFrame based on month and year
            filtered_df = df[df['First Deposit Date'].dt.month == month_num]
            filtered_df = filtered_df[filtered_df['First Deposit Date'].dt.year == year]

            if filtered_df.empty:
                print("No data in this month.")
            else:
                # Convert 'First Deposit Date' back to the string format for display
                filtered_df['First Deposit Date'] = filtered_df['First Deposit Date'].dt.strftime('%d/%m/%Y')
                print("Filtered data:")
                print(filtered_df)

                # Save the filtered data to a CSV file
                filtered_df.to_csv('../step-3/backend_clean.csv', index=False)
                print("Filtered data has been saved to cleaned_backend.csv")
        except ValueError:
            print("No data in this month.")

    # Example usage
    filter_data_by_date_and_save(df)
