import pandas as pd

data = pd.read_csv('atmosphere.csv')

# 分割日期/星期
data[['日期', '星期']] = data['日期'].str.split(' ', expand=True, n=1)
# 去除多余字符
data[['最高温度', '最低温度']] = data[['最高温度', '最低温度']].apply(lambda x: x.str.replace('°', ''))
# 计算下雪天气
data.loc[data['天气'].str.contains('雪'), '下雪吗'] = '是'
# 分割日期时间
data['日期'] = pd.to_datetime(data['日期'])
data[['最高温度', '最低温度']] = data[['最高温度', '最低温度']].astype('int')
data['年份'] = data['日期'].dt.year
data['月份'] = data['日期'].dt.month
data['日'] = data['日期'].dt.day
# 预览
data.sample(5)

# 各城市初雪的时间
s_data = data[data['下雪吗'] == '是']
s_data[(s_data['月份'] >= 9)].groupby('年份').first().reset_index()
# 各城市下雪天气分布
s_data.groupby(['城市', '年份'])['日期'].count().to_frame('下雪天数').reset_index()

# start
data_bj = data[(data['年份'] == 2022) & (data['城市'] == '北京')]
data_bj = data_bj.groupby(['月份', '天气'], as_index=False)['日期'].count()

data_pivot = pd.pivot(data_bj,
                      values='日期',
                      index='月份',
                      columns='天气')
data_pivot = data_pivot.astype('float')
# 按照 索引年月倒序排序
data_pivot.sort_index(ascending=False, inplace=True)

###### 北上广深2021年10月份天气热力图分布
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# 设置全局默认字体 为 雅黑
plt.rcParams['font.family'] = ['Microsoft YaHei']
# 设置全局轴标签字典大小
plt.rcParams["axes.labelsize"] = 14
# 设置背景
sns.set_style("darkgrid", {"font.family": ['Microsoft YaHei', 'SimHei']})
# 设置画布长宽 和 dpi
plt.figure(figsize=(18, 8), dpi=100)
# 自定义色卡
cmap = mcolors.LinearSegmentedColormap.from_list("n",
                                                 ['#95B359', '#D3CF63', '#E0991D', '#D96161', '#A257D0', '#7B1216'])
# 绘制热力图

ax = sns.heatmap(data_pivot, cmap=cmap, vmax=30,
                 annot=True,  # 热力图上显示数值
                 linewidths=0.5,
                 )
# 将x轴刻度放在最上面
ax.xaxis.set_ticks_position('top')
plt.title('北京最近10个月天气分布', fontsize=16)  # 图片标题文本和字体大小
plt.show()
