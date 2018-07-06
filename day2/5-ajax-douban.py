import urllib.request
import urllib.parse
import logging
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

page = int(input('请输入要查看的页码:'))
#开始的页数
start = (page - 1) * 20
limit = 20
data = {
    'start': start,
    'limit': limit,
}

data = urllib.parse.urlencode(data)
logging.debug(data) #'start=0&limit=20'
url = url + data

#构建请求
req = urllib.request.Request(url=url, headers=headers)
#发送请求
res = urllib.request.urlopen(req)
print(res.read().decode('utf-8'))