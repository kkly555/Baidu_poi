import csv
import json

import requests


def main(query, tag, region):  # query关键字 region检索行政区划区域
    base_url = "https://api.map.baidu.com/place/v2/search?"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }
    ak = "8mETgr0IVUy7syq8Axpv9cHQsqAym8ZN"
    data_csv = region + '.csv'
    with open(data_csv, 'w', encoding='UTF-8', newline="") as D:
        csv_head = ['name', 'lng', 'lat', 'address']
        csv_write = csv.DictWriter(D, fieldnames=csv_head)
        csv_write.writeheader()
        for page_num in range(8):
            ask_url(base_url, headers, query, tag, region, ak, page_num, csv_write)


def ask_url(base_url, headers, query, tag, region, ak, page_num, csv_write):  # query关键字
    end_url = base_url + "query=" + query + "&tag=" + tag + "&region=" + region + "&output=json" + "&ak=" + ak \
              + "&coord_type=1" + "&page_size=20" + "&page_num=" + str(page_num)
    html = requests.get(end_url, headers=headers)
    result = html.text
    get_result(result, csv_write)
    # print(html.text)


def get_result(result, csv_write):
    result = json.loads(result)
    results = result['results']
    count = len(results)
    for i in range(count):
        data = results[i]
        name = data['name']
        location = data['location']
        lng = location['lng']
        lat = location['lat']
        address = data['address']
        csv_write.writerow(
            {
                'name': name,
                'lng': lng,
                'lat': lat,
                'address': address
            }
        )


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    query = "酒店"
    tag = ""
    region = "中原区中原西路街道"
    main(query, tag, region)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
