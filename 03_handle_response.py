from datetime import datetime

import requests


def get_res_json(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        print("响应状态码为 200")
        return response.json()  # 解析响应数据为JSON格式
    else:
        # 如果响应不正确，那么抛出响应内容
        print("响应码不为 200，请检查：" + response.text)
        return None


def print_time(time):
    if time is not None:
        print("当前时间：", time)
    else:
        print("请求失败")


def get_time_by_url(urls):
    for key, value in urls.items():
        print(f"正在请求 {key} 的时间...")
        data_raw = get_res_json(value)
        if key == "taobao":
            # 提取字段和值，在 data.t层级下
            timestamp = data_raw['data']['t']
            # 如果 timestamp 不为空
            if timestamp:
                # 格式化一下时间，使其更可读
                formatted_time = datetime.fromtimestamp(int(timestamp) / 1000).strftime("%Y-%m-%d %H:%M:%S")
                print("接口内容判断成功，提取出的时间： " + formatted_time)
        print("接口验证通过")

if __name__ == "__main__":
    urls = {
        "suning": "http://quan.suning.com/getSysTime.do",
        "taobao": "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"
    }
    get_time_by_url(urls)
