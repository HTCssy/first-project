import os
import re
import urllib.request

#下载
def download_img(src, n):
    #获取基本的文件名
    img_name = os.path.basename(src)
    #拼接路径
    filename = os.path.join('../day3/img_meinv', img_name)
    #下载
    urllib.request.urlretrieve(src, filename)
    print(filename + '下载完毕第%s张'%(n))

#发送请求.获取内容
def get_content(req):
    # 构建一个Handler对象
    handler = urllib.request.HTTPHandler()
    # 通过Handler对象构建一个opener对象
    opener = urllib.request.build_opener(handler)
    res = opener.open(req)
    html = res.read().decode('gbk')
    #通过正则拿到图片链接
    pattern = re.compile(r'<i>.*?<img src=(.*?) width=.*?>.*?</i>')
    src_list = pattern.findall(html)
    # print(src_list[0])
    # print(len(src_list))
    n = 0
    for src in src_list:
        #去掉图片链接两边的双引号
        src = src.strip('"')
        n += 1
        download_img(src, n)
#构建请求
def build_url(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    url = url + str(page) + '.html'
    req = urllib.request.Request(url=url, headers=headers)
    return req

def main():
    url = 'http://www.27270.com/ent/meinvtupian/list_11_'
    start = int(input('请输入开始页码:'))
    end = int(input('请输入结束页码:'))
    print('开始下载')
    for page in range(start, end+1):
        req = build_url(url,page)
        get_content(req)

if __name__ == '__main__':
    main()