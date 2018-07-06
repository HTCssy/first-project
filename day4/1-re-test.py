#贪婪模式和非贪婪模式(懒惰模式)
import re
str1 = '<div>哈哈<div>呵呵</div>啦啦<div>嘻嘻</div>嘿嘿</div>'
#匹配一个或者多个
# res1 = re.match('<div>.*</div>', str1)
#匹配0个或者一个
res1 = re.match('<div>.*?</div>', str1)
print(res1)
print('------------------')
#子模式
str2 = 'goodgood678study99'
res2 = re.match('(good){2}(\d+)study(\d+)', str2)
print(res2)
print(res2.group(1))#good
print(res2.group(2))#678
print(res2.group(3))#99

print('-------------------------')
str3 = '''good good study
day day up
happy every day
nice to meet you
good good is very good
'''
#匹配一行
# res3 = re.compile('^good', re.S)
#匹配多行
res3 = re.compile('^good', re.M)
result = res3.search(str3)
print(result)
print(result.group())
