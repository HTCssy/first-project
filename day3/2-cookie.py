import os
import urllib.request

url = 'https://weibo.com/3008370055/profile?rightmod=1&wvr=6&mod=personinfo&is_all=1'

headers = {
'Cookie': 'SINAGLOBAL=9578488474880.035.1529628614387; YF-Ugrow-G0=ea90f703b7694b74b62d38420b5273df; login_sid_t=2484cceb1bef3ffe5ff88abb5028046f; cross_origin_proto=SSL; YF-V5-G0=572595c78566a84019ac3c65c1e95574; WBStorage=5548c0baa42e6f3d|undefined; wb_view_log=1536*8641.25; _s_tentry=passport.weibo.com; UOR=,widget.weibo.com,www.sina.com.cn; Apache=8168189822498.966.1530674259457; ULV=1530674259464:3:1:1:8168189822498.966.1530674259457:1530014068579; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW95Da4KkuQ7DIu0_UIQq4z5JpX5K2hUgL.Foe7ehn0S057SK-2dJLoI7yJqPx_qgRpeBtt; ALF=1562210284; SSOLoginState=1530674285; SCF=AkDCqEfQ5u2Y6vhD0F1Z7Egwn1-BVlNYuu6vf3rRqYejZVzRndubzte3bfANxmvqApkcXmKhTB8elLUy8btoKJk.; SUB=_2A252OEw9DeRhGeVO61oS9y7MzjmIHXVVTDr1rDV8PUNbmtBeLU32kW9NTVGec2jdsyfQW4MaJUXynaHiEz9r9mK3; SUHB=0tKa0_SfNoJfOo; un=18612032591; wvr=6; YF-Page-G0=a478b43c3fd6f5a258feb64dc37bff16; wb_view_log_3008370055=1536*8641.25',
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'

}
req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
# print(res.read().decode('utf-8'))
filename = os.path.join('../day3', 'senl.html')
with open(filename, 'wb') as f:
    f.write(res.read())