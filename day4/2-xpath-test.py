from lxml import etree
#本地的html文件
d_tree = etree.parse('testXpath.html')
print(d_tree)
#获取所有的li节点
res = d_tree.xpath('//li')
print(res)
#获取所有li节点的class属性
res1 = d_tree.xpath('//li/@class')
print(res1)
#获取每一个ol节点最后一个li节点的文本内容
res2 = d_tree.xpath('//ol/li[last()]/text()')
print(res2)
#获取每一个ol节点最后一个li节点的最后一个文本内容
res3 = d_tree.xpath('//ol/li[last()]/text()')[2]
print(res3)
#拿到http://mi.com值
res4 = d_tree.xpath('//div[@class="hh"]/a/@href')[0]
print(res4)
#拿到雷军文本值
res5 = d_tree.xpath('//div[@class="hh"]/a/text()')[0]
print(res5)
#找到id为pp的div中ol节点里面class以h开头的li节点
res6 = d_tree.xpath('//div[@id="pp"]/ol/li[starts-with(@class, "h")]')
print(res6)
#找到id为pp的div中ol节点里面class以h开头的第2个li节点文本
res7 = d_tree.xpath('//div[@id="pp"]/ol/li[starts-with(@class, "h")]/text()')[1]
print(res7)



'''
https://www.qiushibaike.com/text/page/4/

//div[@id="content-left"]/div/div/a/img/@src

//div[@id="content-left"]/div/div/a/h2/text()
'''