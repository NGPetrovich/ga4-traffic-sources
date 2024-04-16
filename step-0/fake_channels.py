import pandas as pd

data = {
    'GA4 Channel Name': ['(direct) / (none)', 'google / organic', 'google / cpc', 'lalalala.be / referral', 'iOS', 'Android', 'Macintosh'],
    'Channel Name': ['Direct', 'Google Organic', 'Google Ads', 'Lalala website', 'iOS App', 'Android App', 'iOS App']
}

df = pd.DataFrame(data)

output_file_path = '../step-7/fake_channels_data.csv'
df.to_csv(output_file_path, index=False)

print(f"CSV file has been created at {output_file_path}.")
