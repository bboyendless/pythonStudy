import requests

def get_time(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()  # 解析响应数据为JSON格式
    else:
        return None

def print_time(data):
    if data is not None:
        print("当前时间：", data)
    else:
        print("请求失败")

def get_time_by_url(urls):
    for key, value in urls.items():
        print(f"正在请求 {key} 的时间...")
        data = get_time(value)
        print_time(data)

if __name__ == "__main__":
    urls = {
        "suning": "http://quan.suning.com/getSysTime.do",
        "taobao": "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"
    }
    get_time_by_url(urls)
