# 第一课——接口
什么是接口？
接口就是你在绝大多数页面打开「开发者模式」——「网络」中看到的内容：
接口由什么组成？
请求URL：HTTP接口通过URL来标识资源或操作，URL通常包含主机名、端口号、路径和查询参数等信息。下列这些都是接口
`https://venus.meetwhale.com/graphql
http://alivia.abc.com:31170/graphql/api/market_Marketing/launchActivityGame`

HTTP方法：HTTP接口使用HTTP协议定义的方法来表示对资源的操作，常见的HTTP方法包括GET、POST、PUT、DELETE等。
请求头：HTTP接口可以包含一系列请求头，用来传递额外的请求信息，如Content-Type、Authorization等。
`content-type: application/json
authorization: cju0EJYnQzq3_LoGDi_6cA`

请求体：某些HTTP接口需要在请求体中传递数据，例如POST和PUT请求，请求体通常使用JSON、XML等格式进行编码。
响应头：HTTP接口的响应也包含一系列响应头，用来传递额外的响应信息，如Content-Type、Content-Length等。
响应体：HTTP接口的响应主体包含了请求所期望的数据，响应体通常使用JSON、XML等格式进行编码。
怎么调接口？
最简单的方法：mac打开「终端」，windows打开「cmd」或「powershell」 输入：

`curl http://quan.suning.com/getSysTime.do`

你会获得服务器返回的当前时间
其他依赖工具: postman/apifox 等等，使用方法不再赘述
代码调用，python、java、go等等代码均可，下面以python示例
实操部分：
请移步
https://github.com/bboyendless/pythonStudy
clone代码，在本地成功运行一次


# 第二课——方法和参数化接口
上节课大家使用了request来构建一个接口访问的代码，同时进行了简单的返回判断，这已经很好了。
不过接下来，我们应该对这段代码进行优化，想让这个方法变得更通用，我们应该把他抽离出来
```python
import requests

url = "http://quan.suning.com/getSysTime.do"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("请求失败，状态码为：", response.status_code)
```
**改写成：**
```python
import requests

def get_time(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.text)
        return response
    else:
        print("请求失败，状态码为：", response.status_code)
```
**在python中，def代表定义一个方法，def get_time(url)，代表这个方法名叫get_time，输入参数url，冒号后面代表这个方法的代码，
如果有return，就代表该方法有返回，返回是return后的内容**

这样这段代码就有了一个出入口，输入url，输出这个url的请求结果。

但是实际工作中，我们会遇到多个url，或者请求参数依据环境/case变化的情况，所以接下来，我们通过把url参数化来实现一个简单的参数化：

```python
import requests

# 将url设计成满足不同调用需求的参数
urls = {"suning":"http://quan.suning.com/getSysTime.do",
        "taobao":"http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"}

def get_time_by_url(urls):
    response = requests.get(url=urls)
    if response.status_code == 200:
        print(response.text)
    else:
        print("请求失败，状态码为：", response.status_code)
```
**python中的这种写法叫字典(dict): url={"a":"b","c":"d"}，类似于json
取用的时候可以方便的使用url["a"]去取用，返回的值是"b"**

这样，我们就可以实现参数化发送请求了，我们可以在方法下编写这段代码调试/运行，至于为什么要写`if __name__ == "__main__"`这个以后再说

```
if __name__ == "__main__":
   get_time_by_url(urls=urls["taobao"])
```

实操部分：
clone代码到本地，在02_requests_with_params.py中，为urls新增一个字典对应键值：
"qq": "http://vv.video.qq.com/checktime?otype=json"，
并在 `if __name__ == "__main__"` 中调用它

# 第三课——处理接口响应数据
在第一和第二课中，你已经学习了如何发送接口请求并获取响应。现在可以进一步学习如何解析和提取响应数据中的有用信息。

主题和内容：

JSON数据解析：学习如何解析接口响应中的JSON数据。介绍常用的JSON解析库，例如json模块、requests库的json()方法以及其他第三方库。

1. 响应状态码处理：描述接口的响应是什么状态的代码

   **常见响应状态码**：

| 状态码 | 描述                      |
|-----|-------------------------|
| 1** | 信息，服务器收到请求，需要请求者继续执行操作  |
| 2** | 成功，操作被成功接收并处理           |
| 3** | 重定向，需要进一步的操作以完成请求       |
| 4** | 客户端错误，请求包含语法错误或无法完成请求   |
| 5** | 服务器错误，服务器在处理请求的过程中发生了错误 |

python 中，常见判断响应状态码是否为 200的方法：

```  python     
   if response.status_code == 200:
    # 响应成功处理逻辑
    ...

```

2. 数据提取和断言：如何从接口响应的JSON数据中提取所需的字段和值，以及如何使用断言进行结果的验证和校验。

* 使用json模块：使用json模块的loads()函数将JSON字符串解析为Python对象，然后通过字典键值的方式提取所需字段和值。
 例如上节课我们已经知道 taobao 返回的格式是：
`{'api': 'mtop.common.getTimestamp', 'v': '*', 'ret': ['SUCCESS::接口调用成功'], 'data': {'t': '1688546655186'}}`
那么上节课的打印方式就可以改为：

```python
def get_time_by_url(urls):
    for key, value in urls.items():
        print(f"正在请求 {key} 的时间...")
        data_raw = get_time(value)
        if key == "taobao":
           # 提取字段和值，在 data.t层级下
           time = data_raw['data']['t']
           print("提取出的时间： " + time)
        print_time(data_raw)
```

* 使用requests库的json()方法：requests库提供了方便的json()方法，它将响应的JSON数据解析为Python对象。
应用到我们的 case 中也是类似的方法，不再赘述
```python
# 将响应的JSON数据解析为Python对象
response_data = response.json()

# 提取字段和值
field_value = response_data['field']
```
* 使用第三方库：除了上述方法，还有一些第三方库如pyjq、jq等，可以根据需求选择合适的库进行数据提取。

## 时机已经基本成熟了，我们来为这个接口写个简单的验证：
我们先把对 状态码 的校验提取出来，如果状态码不为 200，则直接返回 response 内容，看看问题出在哪 ：
```python
def get_res_json(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        print("响应状态码为 200")
        return response.json()  # 解析响应数据为JSON格式
    else:
        # 如果响应不正确，那么抛出响应内容
        print("响应码不为 200，请检查：" + response.text)
        return None
```
再对实际的接口请求方法进行判断
```python
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
```
运行的结果如下：
```angular2html
正在请求 suning 的时间...
响应状态码为 200
接口验证通过
正在请求 taobao 的时间...
响应状态码为 200
接口内容判断成功，提取出的时间： 2023-07-05 17:35:27
接口验证通过
```
总结：我们目前有两个接口，我们对其中一个名为 taobao 的接口做了相对完善的接口自动化用例判断
1. 我们抽取出了公共的用来判断接口状态码的get_res_json模块，状态码正确就返回json 格式的 res，错误就直接返回 res
2. 如果判断是 taobao 的接口，我们就对接口返回的内容进一步提取，判断时间是否为空
3. 打印内容，判断接口是否成功

实操：为 suning 接口编写自动化用例判断，要求：判断返回内容 sysTime1和sysTime2 是否相等, 返回内容：
`{'sysTime2': '2023-07-05 17:43:20', 'sysTime1': '20230705174320'}
`