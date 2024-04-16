import pandas as pd
import numpy as np
import random

num_entries = 800

unique_ids = set()
while len(unique_ids) < num_entries:
    potential_id = np.random.randint(12345678, 12347999)
    unique_ids.add(potential_id)

device_brand_options = ["Apple", "Google", "OPPO", "Huawei", "Samsung", "Xiaomi", "OnePlus", "Motorola", "Apple"]
operating_system_options = ["iOS", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Macintosh"]

data = {
    'FTD Attempted NATIVE User ID': list(unique_ids),
    'Device brand': [random.choice(device_brand_options) for _ in range(num_entries)],
    'Operating system': [random.choice(operating_system_options) for _ in range(num_entries)],
    'Event value': np.random.randint(1, 4001, num_entries)
}

df = pd.DataFrame(data)

comments = [
    "# ----------------------------------------",
    "# www.nikita.SaysHi - GA4",
    "# iOS App REGs and FTDs-FTDs_ONLY",
    "# 20240301-20240312",
    "# ----------------------------------------"
]

summary_row = ",,,124142,Grand total,"

comments_str = '\n'.join(comments) + '\n'

new_file_path = '../step-5/fake_native_data.csv'

csv_data = df.to_csv(index=False, header=False)

with open(new_file_path, 'w', newline='') as file:
    file.write(comments_str)
    file.write('\n')
    file.write('FTD Attempted NATIVE User ID,Device brand,Operating system,Event value,\n')
    file.write(summary_row + '\n')
    file.write(csv_data)

print(f"CSV file '{new_file_path}' has been created with the specified formatting.")
