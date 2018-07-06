import urllib.request
url = 'http://www.baidu.com'
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.10 Safari/537.36"
}
#构建请求
req = urllib.request.Request(url=url, headers=headers)
#发送请求
res = urllib.request.urlopen(req)
print(res.read().decode('utf-8'))

#直接写入
# urllib.request.urlretrieve("http://www.baidu.com", filename='file1.html')
