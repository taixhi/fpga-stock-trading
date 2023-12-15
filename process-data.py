import pandas as pd

# get the ETH data
eth_df = pd.read_csv("/home/pi/final-project/data/ETH_1min.csv")

# get the BTC data
btc_df = pd.read_csv("/home/pi/final-project/data/coinbaseUSD_1-min_data.csv")

# Convert Unix timestamp to datetime
eth_df['timestamp'] = pd.to_datetime(eth_df['Unix Timestamp'], unit='s')
btc_df['timestamp'] = pd.to_datetime(btc_df['Unix Timestamp'], unit='s')

# Merge DataFrames on timestamp
merged_df = pd.merge(eth_df, btc_df, on='timestamp', suffixes=('_eth', '_btc'))

# Filter rows by date
selected_date = pd.Timestamp('2016-05-01')
filtered_df = merged_df[merged_df['timestamp'].dt.date == selected_date.date()]
filtered_df.to_csv('/home/pi/final-project/data/raw_merge.csv', index=False)
filtered_df.rename(columns = {'Open_eth': 'eth', 'Open_btc': 'btc'},inplace=True)
filtered_df.to_csv('/home/pi/final-project/data/final_merge.csv', index=False)
