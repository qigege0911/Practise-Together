import re
'用正则表达式筛选出，只包含字母、空格和数字的行，结果是一个列表，每个元素是一行'
s='''
i love you not because
12sd 34er*% 56
df e4*%$ 5@%!4434
sfi hi q94 729
'''
result=re.findall(r'\n[\w\s]+\n',s)
print(result)
