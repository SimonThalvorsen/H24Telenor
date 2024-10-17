import pandas as pd
import glob

path = "./network-performance/OoklaMobilePerformance_Telenor/"

all_files = glob.glob(path + "*.csv")

dataframes = []

for filename in all_files:
    df = pd.read_csv(filename, low_memory=True)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

combined_df = combined_df.drop_duplicates()

failures_summary = combined_df.groupby("attr_place_formatted_address")[
    "num_connections_failed"
].agg(["mean", "sum"])

failures_summary = failures_summary[failures_summary["sum"] > 100]

top_15_failures_sum100 = failures_summary.sort_values(by="mean", ascending=False).head(
    15
)
failures_summary = failures_summary[failures_summary["sum"] > 500]

top_15_failures_sum500 = failures_summary.sort_values(by="mean", ascending=False).head(
    15
)

print("Top 15 failed_connections sum >= 100")
print(top_15_failures_sum100)

print("\n\nTop 15 failed_connections sum >= 500")
print(top_15_failures_sum500)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.barplot(data=top_15_failures_sum100.reset_index(), 
            x='mean', 
            y='attr_place_formatted_address', 
            palette='viridis', 
            ax=axes[0])
axes[0].set_title('Top 15 Places with Highest Mean Failed Connections (Sum >= 100)')
axes[0].set_xlabel('Mean Failed Connections')
axes[0].set_ylabel('Location')

sns.barplot(data=top_15_failures_sum500.reset_index(), 
            x='mean', 
            y='attr_place_formatted_address', 
            palette='plasma', 
            ax=axes[1])
axes[1].set_title('Top 15 Places with Highest Mean Failed Connections (Sum >= 500)')
axes[1].set_xlabel('Mean Failed Connections')
axes[1].set_ylabel('Location')

plt.tight_layout()
plt.show()
