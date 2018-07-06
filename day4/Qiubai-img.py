import json
import urllib.request
from lxml import etree

from utility.reptile_uti import build_req, get_data


def json_text(html_list, name_list):
    result = {}
    data = []
    for i in range(len(name_list)):
        img_url = 'http:'+html_list[i]
        name = name_list[i].strip('\n')
        data.append({'img_url': img_url,
                     'name': name})
    result.update(data=data)
    data = json.dumps(result, ensure_ascii=False)
    with open('../day4/Qiubai/img.json', 'w', encoding='utf-8') as f:
        f.write(data)


def main():
    start = int(input('请输入开始页码:'))
    end = int(input('请输入结束页码:'))
    url = 'https://www.qiushibaike.com/text/page/'
    print('开始下载')
    for page in range(start, end + 1):
        url = url + str(page)
        req = build_req(url)
        html = get_data(req)
        html_etree = etree.HTML(html)
        html_list = html_etree.xpath('//div[@id="content-left"]/div/div/a/img/@src')
        name_list = html_etree.xpath('//div[@id="content-left"]/div/div/a/h2/text()')
        json_text(html_list, name_list)

if __name__ == '__main__':
    main()