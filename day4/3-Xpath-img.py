import os
import urllib.request

from lxml import etree
def download_img(url_list, namelist):
    n = 0
    dirpath = '../day4/hunsha'
    for i in range(len(namelist)):
        #截取后缀名
        suffix = os.path.splitext(url_list[i])[-1]
        #得到图片全路径
        file_path = os.path.join(dirpath, namelist[i]) + suffix
        try:
            urllib.request.urlretrieve(url_list[i], file_path)
            n += 1
            print('{}--下载完毕第{}张'.format(file_path, n))
        except Exception as e:
            print('{}--图片丢失'.format(file_path))

def get_data(req):
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)
    res = opener.open(req)
    html = res.read().decode('utf-8')
    html_etree = etree.HTML(html)
    url_list = html_etree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    name_list = html_etree.xpath('//div[@id="container"]/div/div/a/img/@alt')
    download_img(url_list, name_list)
def build_req(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=headers)
    return req

def main():
    start = int(input('请输入开始页码:'))
    end = int(input('请输入结束页码:'))
    url_tmp = 'http://sc.chinaz.com/tupian/hunsha'
    print('开始下载')
    for page in range(start, end+1):
        if page != 1:
            url = url_tmp+"_"+str(page)+'.html'
        else:
            url = url_tmp+'.html'
        req = build_req(url)
        get_data(req)


if __name__ == '__main__':
    main()