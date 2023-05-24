import requests

# 将url设计成满足不同调用需求的参数，python中的这种写法叫字典(dict): url={"a":"b","c":"d"}，类似于json
# 取用的时候可以方便的使用url["a"]去取用，返回的值是"b"
urls = {"suning":"http://quan.suning.com/getSysTime.do",
        "taobao":"http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"}

def get_time(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.text)
        return response
    else:
        print("请求失败，状态码为：", response.status_code)


def get_time_by_url(urls):
    response = requests.get(url=urls)
    if response.status_code == 200:
        print(response.text)
    else:
        print("请求失败，状态码为：", response.status_code)


if __name__ == "__main__":

   get_time_by_url(urls=urls["taobao"])