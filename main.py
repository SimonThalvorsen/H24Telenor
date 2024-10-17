import pandas as pd
import glob

# Path to your CSV files
path = "./network-performance/OoklaMobilePerformance_Telenor/"

# Gather all CSV files
all_files = glob.glob(path + "*.csv")

# List to hold DataFrames
dataframes = []

# Read and append each CSV file into the list
for filename in all_files:
    df = pd.read_csv(filename)
    dataframes.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Clean and preprocess
combined_df = combined_df.drop_duplicates()
# Convert date columns if necessary

# Analyze
average_speed_per_region = combined_df.groupby("attr_place_formatted_address")[
    "num_connections_failed"
].mean()
print(average_speed_per_region)
