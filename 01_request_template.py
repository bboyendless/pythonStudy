import requests

url = "http://quan.suning.com/getSysTime.do"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("请求失败，状态码为：", response.status_code)

def get_time(url):
    response = requests.get(url=url)

    if response.status_code == 200:
        print(response.text)
        return response
    else:
        print("请求失败，状态码为：", response.status_code)
