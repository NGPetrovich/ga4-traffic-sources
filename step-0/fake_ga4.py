import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Helper functions
def generate_random_date_strings(start_date, end_date, num_entries):
    delta = end_date - start_date
    random_dates = []
    for _ in range(num_entries):
        random_date = start_date + timedelta(days=random.randint(0, delta.days))
        random_dates.append(random_date.strftime('%Y%m%d'))
    return random_dates

# Criteria for data generation
start_date = datetime.strptime('20240301', '%Y%m%d')
end_date = datetime.strptime('20240312', '%Y%m%d')
num_entries = 100  # Adjust as needed

# Generate random data based on the criteria
random_dates = generate_random_date_strings(start_date, end_date, num_entries)
keyword_text_options = ['(not set)', 'lalala', 'momomo', 'dododo']
campaign_options = ['(direct)', '(organic)', 'betting']
source_medium_options = ['(direct) / (none)', 'google / organic', 'google / cpc', 'lalalala.be / referral']

data = {
    'Date': random_dates,
    'First user Google Ads keyword text': [random.choice(keyword_text_options) for _ in range(num_entries)],
    'Campaign': [random.choice(campaign_options) for _ in range(num_entries)],
    'Source/Medium': [random.choice(source_medium_options) for _ in range(num_entries)],
    'FTD Attempted User ID': np.random.randint(12345678, 12349999, num_entries),
    'Total users': np.random.randint(1, 3, num_entries),
    'Event value': np.random.randint(1, 4001, num_entries)
}

df = pd.DataFrame(data)

# Define comments and header structure
comments = [
    "# ----------------------------------------",
    "# www.nikita.SaysHi - GA4",
    "# ftd_attempted-Keywords from Google Ads",
    "# 20240301-20240312",
    "# ----------------------------------------"
]

# Adding a summary/info row similar to row 8 from the test-real2.csv
summary_row = ",,,,,124,124142,Grand total,"

# Convert comments to a single string with newlines
comments_str = '\n'.join(comments) + '\n'

# Define the file path for the new CSV file
new_file_path = '../step-1/fake_data.csv'

csv_data = df.to_csv(index=False, header=False)

# Save the DataFrame with comments and the summary row, ensuring no extra newlines
with open(new_file_path, 'w', newline='') as file:
    file.write(comments_str)
    file.write('\n')  # Blank line before headers
    file.write('Date,First user Google Ads keyword text,Campaign,Source/Medium,FTD Attempted User ID,Total users,Event value,\n')
    file.write(summary_row + '\n')  # Include the summary/info row
    file.write(csv_data)  # Write the CSV data string directly

print(f"CSV file '{new_file_path}' has been created with the specified formatting.")
