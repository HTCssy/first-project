import urllib.request
#构建请求
def build_req(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=headers)
    return req

#发送请求.读取数据
def get_data(req):
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)
    res = opener.open(req)
    html = res.read().decode('utf-8')
    return html
