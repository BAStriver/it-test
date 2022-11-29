import requests
import parsel
import csv

with open('atmosphere.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["日期", "最高温度", "最低温度", "天气", "风向", "城市"])
city_list = [54511, 58362, 59287, 59493]
for city in city_list:
    for year in range(2015, 2023):
        for month in range(1, 13):
            url = f'https://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D={city}&areaInfo%5BareaType%5D=2&date%5Byear%5D={year}&date%5Bmonth%5D={month}'

            response = requests.get(url=url)
            json_data = response.json()

            # 结构化数据解析
            html_data = json_data['data']
            selector = parsel.Selector(html_data)
            # 正则 css xpath json字典数据解析
            tr_list = selector.css('.history-table tr')
            # tr_list[1:] 从列表的第二个元素开始取
            for tr in tr_list[1:]:
                # <X>fhwaeuifhwiuf</X>
                td = tr.css('td::text').getall()
                if td[2] == '°':
                    td[2] = td[1]
                if city == 54511:
                    td.append("北京")
                elif city == 58362:
                    td.append("上海")
                elif city == 59287:
                    td.append("广州")
                elif city == 59493:
                    td.append("深圳")
                print(td)
                with open('atmosphere.csv', mode='a', encoding='utf-8', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(td)

