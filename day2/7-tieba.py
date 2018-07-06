import os
import urllib.request
import urllib.parse
import logging

#拼接url构建请求对象
def build_url(url, page, tname, headers):
    data = {
        'kw': tname,
        'pn': (page-1)*50
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    #路径
    # url += data
    req = urllib.request.Request(url=url, headers=headers, data=data)
    return req

#发送请求
def download(req, page):
    res = urllib.request.urlopen(req)
    dirname = '../day2/tieba'
    filename = '第'+str(page)+'页.html'
    filepath = os.path.join(dirname, filename)
    with open(filepath, 'wb') as fw:
        fw.write(res.read())

def main():
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))
    tname = input('请输入贴吧名:')
    url = 'http://tieba.baidu.com/f?&ie=utf-8&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    for page in range(start_page, end_page):
        #构建请求
        req = build_url(url, page, tname, headers)
        download(req, page)

if __name__ == '__main__':
    main()