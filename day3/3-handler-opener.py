import urllib.request
#构建一个Handler对象
handler = urllib.request.HTTPHandler()
#通过Handler对象构建一个opener对象
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
#构建请求
req = urllib.request.Request(url=url, headers=headers)
#发送请求
res = opener.open(req)
#读取数据
print(res.read().decode('utf-8'))