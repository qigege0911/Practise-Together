import re

'主要用到re.findall函数，其用法可以去百度，另外正则表达式的用法请看廖雪峰的Python教程' \
'链接：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000'

'''请用正则表达式，找出下面字符串中所有c开头的单词，结果是一个列表，列表里面每一个元素是一个单词' \
'得出的列表应该是
['curtain','clear','case','certain']
'''



s =\
'''
    And now, the end is near　　And so I face the final curtain　　My friend, I'll make it clear
    I'll state my case, of which I'm certain
'''
result=re.findall(r'\b[c][a-z]+',s)
print(result)