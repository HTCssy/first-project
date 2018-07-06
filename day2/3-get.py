import os
import urllib.parse
import urllib.request

kw = input('请输入您要搜索的内容')
#编码 ,只争对字符串
kw = urllib.parse.quote(kw)
#拼接url
url = 'https://www.baidu.com/s?wd='+ kw
print(url)

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

#构建请求对象
req = urllib.request.Request(url=url, headers=headers)
#发送请求
res = urllib.request.urlopen(req)

#进行数据的读写保存
# with open('china.html','wb') as fw:
#     fw.write(res.read())
filename = os.path.join('../day2', 'china.html')
with open(filename,'w',encoding='utf-8') as fw:
    fw.write(res.read().decode('utf-8'))