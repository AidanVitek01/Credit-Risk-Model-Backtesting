# For Python Scripts

import pandas as pd

df = pd.read_csv("data/raw/cs-training.csv")

print(df.head()) #Sanity Check
print(df.isna().sum()) # Observe NA patterns
