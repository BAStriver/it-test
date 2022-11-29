from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("customer1997.csv", encoding='utf-8', dtype=str)
df = pd.DataFrame(df, columns=['Monetary'])
section = np.array(range(0, 105, 5))
result = pd.cut(df['Monetary'], section)
count = pd.value_counts(result, sort=False)
fig, ax = plt.subplots()
plt.style.use('classic')
ax.set_xlim(0, 100)
rect1 = plt.bar(np.arange(2.5, 100, 5), count, width=5)
for r in rect1:
    ax.text(r.get_x(), r.get_height(), r.get_height())
plt.show()