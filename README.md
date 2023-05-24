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
**在python中，def代表定义一个方法，def get_time(url)，代表这个方法名叫get_time，输入参数url，冒号后面代表这个方法的代码，如果有return，就代表该方法有返回，返回是return后的内容**

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
clone代码到本地，在02_requests_with_params.py中，为urls新增一个字典对应键值："qq": "http://vv.video.qq.com/checktime?otype=json"，
并在 `if __name__ == "__main__"` 中调用它
