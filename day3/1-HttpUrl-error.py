import urllib.request
import urllib.error

# url = 'http://www.baidu.com/'
# url = 'https://www.baidu-hhhh.com/' 制造UrlError
# 制造HttpError
url = 'https://blog.csdn.net/whd526/article/details/52279108'

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
req = urllib.request.Request(url=url, headers=headers)
try:
    res = urllib.request.urlopen(req)
    print(res.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('1-http-error')
    print(e)
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print('2-url-error')
    print(e)

except Exception as e:
    print('3-exception')

print('--已经到最后了--')
