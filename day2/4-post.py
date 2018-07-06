import json
import os
import urllib.request
import urllib.parse
import logging

url = 'http://fanyi.baidu.com/sug/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
kw = input('请输入要翻译的词')
data = {
    'kw': kw
}
#编码动作
# data = urllib.parse.urlencode(data)
# print(data)  结果 kw=%E4%BD%A0%E5%A5%BD
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)  #  b'kw=%E4%BD%A0%E5%A5%BD'
#构建请求
req = urllib.request.Request(url=url, headers=headers, data=data)
#发送请求
res = urllib.request.urlopen(req)
#读取响应数据
result = res.read().decode('utf-8')
# print(result)
#把json字符串转为python字典
json_obj = json.loads(result)
#把python字典转为json字符串
str = json.dumps(json_obj, ensure_ascii=False)
# print(json)
filename = os.path.join('../day2', 'baidufy.json')
logging.debug(filename)
with open(filename, 'w', encoding='utf-8') as fw:
    fw.write(str)