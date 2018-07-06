import urllib.request
import urllib.parse
import logging
url ='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers ={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

data = {
'cname':'北京',
    'pid': '' ,
    'pageIndex': '1',
    'pageSize': '10'
}
data=urllib.parse.urlencode(data).encode('utf-8')
logging.debug(data)

req=urllib.request.Request(url=url,headers=headers,data=data)

res=urllib.request.urlopen(req)
print(res.read().decode('utf-8'))