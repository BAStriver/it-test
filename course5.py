import pandas as pd
from mlxtend.frequent_patterns import apriori

dataset = pd.read_csv("shopping_basket.csv")

df = dataset.drop(dataset.columns[0:7], axis=1)

frequent_items = apriori(df, min_support=0.05, use_colnames=True, max_len=4).sort_values(by='support', ascending=False)

print(frequent_items)
