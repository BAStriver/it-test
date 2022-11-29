import pandas as pd
from statsmodels import api as sm

df = pd.read_csv("customer1997.csv")
data = df
# 模型1
x_1 = sm.add_constant(data.loc[:,['Frequency']])
print(x_1)
y_1=data['Monetary']
model_1=sm.OLS(y_1,x_1)
result_1 = model_1.fit()
print(result_1.summary())
