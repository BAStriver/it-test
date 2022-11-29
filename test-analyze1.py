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
# print(data.sample(5))

# 各城市初雪的时间
s_data = data[data['下雪吗'] == '是']
s_data[(s_data['月份'] >= 9)].groupby('年份').first().reset_index()
# 各城市下雪天气分布
s_data.groupby(['城市', '年份'])['日期'].count().to_frame('下雪天数').reset_index()

# print(s_data)

beijing = []
shanghai = []
guangzhou = []
shenzhen = []

dataList = data.values.tolist()
for num in range(0, len(dataList)):
    # print("---------> ", num)
    items = dataList[num]
    # [Timestamp('2015-01-01 00:00:00'), 4, -6, '晴', '无持续风向微风', '北京', '周四', nan, 2015, 1, 1]
    # 2022年北上广深的10月气温折线图
    if items[8] == 2022 and items[9] == 10:
        if items[5] == '北京':
            beijing.append((items[1] + items[2]) / 2)
        elif items[5] == '上海':
            shanghai.append((items[1] + items[2]) / 2)
        elif items[5] == '广州':
            guangzhou.append((items[1] + items[2]) / 2)
        elif items[5] == '深圳':
            shenzhen.append((items[1] + items[2]) / 2)

import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams["axes.labelsize"] = 14
fig, ax = plt.subplots()
ax.plot(beijing, c='red', label="北京")
ax.plot(shanghai, c='green', label="上海")
ax.plot(guangzhou, c='blue', label="广州")
ax.plot(shenzhen, c='gray', label="深圳")
ax.set_title("2022年北上广深的10月每日平均气温折线图", fontsize=24)
ax.set_xlabel('日期(10月)', fontsize=16)
ax.set_ylabel("温度(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.legend()

plt.show()
