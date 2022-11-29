import pandas as pd

dataset = pd.read_csv("shopping_basket.csv")
# print(dataset.sample(5))

df = dataset.drop(dataset.columns[0:7], axis=1)
print(df)
