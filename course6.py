import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

dataset = pd.read_csv("shopping_basket.csv")

df = dataset.drop(dataset.columns[0:7], axis=1)

frequent_items = apriori(df, min_support=0.05, use_colnames=True, max_len=4).sort_values(by='support', ascending=False)

ass_rule = association_rules(frequent_items, metric='confidence', min_threshold=0.7)
ass_rule.sort_values(by='leverage', ascending=False,inplace=True)
print(ass_rule)
