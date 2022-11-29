import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels import api as sm

df = pd.read_csv("customer1997.csv")
data = df
# print(data.columns)
# print(data['Monetary'].describe())

import matplotlib.pyplot as plt
x = data['Frequency']
y = data['Monetary']
plt.scatter(x, y)
# plt.show()

print(data.corr())
