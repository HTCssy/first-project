#ip代理
import os
import urllib.request
url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'

headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0'
}
req = urllib.request.Request(url=url, headers=headers)
#配置代理ip
handler = urllib.request.ProxyHandler({'http':'116.25.225.72:9999'})
#创建opener对象
opener = urllib.request.build_opener(handler)
#发送请求
res = opener.open(req)

filename = os.path.join('../day3','ip_dl.html')
with open(filename, 'wb') as f:
    f.write(res.read())
