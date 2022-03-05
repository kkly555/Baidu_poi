import requests


def main(query, tag, region):  # query关键字 region检索行政区划区域
    base_url = "https://api.map.baidu.com/place/v2/search?"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }
    ak = "8mETgr0IVUy7syq8Axpv9cHQsqAym8ZN"
    ask_url(base_url, headers, query, tag, region, ak)


def ask_url(base_url, headers, query, tag, region, ak):  # query关键字
    end_url = base_url + "query=" + query + "&tag=" + tag + "&region=" + region + "&output=json" + "&ak=" + ak + "&coord_type=1"
    html = requests.get(end_url, headers=headers)
    print(html.text)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    query = "美食"
    tag = ""
    region = "郑州中原区"
    main(query, tag, region)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
