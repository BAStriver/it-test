import pandas as pd
from statsmodels import api as sm

df = pd.read_csv("customer1997.csv")
data = df
# 模型2
x_2 = sm.add_constant(data.loc[:,['total_children', 'Frequency']])
y_2=data['Monetary']
model_2=sm.OLS(y_2,x_2)
result_2 = model_2.fit()
print(result_2.summary())
