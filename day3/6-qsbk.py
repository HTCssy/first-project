import os
import re
import urllib.request

#下载
def download_img(img_url):
    dir_path ='./qiubai'
    #获得基本的文件名
    img_name=os.path.basename(img_url)
    file_path=os.path.join(dir_path,img_name)
    #下载
    urllib.request.urlretrieve(img_url,file_path)
    print(file_path+'下载完毕')
#获取内容
def get_content(req):
    res=urllib.request.urlopen(req)
    html=res.read().decode('utf-8')
    #通过正则拿到图片链接
    pattern = re.compile(r'<div class="thumb">.*?<img src=(.*?) alt=.*?>.*?</div>', re.S)
    src_list=pattern.findall(html)
    # print(len(src_list))
    for src in src_list:
        #去掉图片链接2边的双引号
        src=src.strip('"')
        img_url ='https:'+src
        download_img(img_url)

#构建请求对象并返回
def build_url(url,page):
    url=url+str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0'
    }
    req=urllib.request.Request(url=url,headers=headers)
    return req

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page=int(input('请输入开始页码:'))
    end_page=int(input('请输入结束页码:'))
    print('开始下载')
    for page in range(start_page,end_page+1):
        req = build_url(url,page)
        get_content(req)

if __name__ =='__main__':
    main()