import http.cookiejar

import urllib.request
import urllib.parse

#创建一个cookiejar对象
cookie = http.cookiejar.CookieJar()

#通过Cookiejar对象生成handler对象
handler = urllib.request.HTTPCookieProcessor(cookie)
#通过handler对象创建opener对象
opener = urllib.request.build_opener(handler)




