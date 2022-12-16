# 注释
# 单行注释
 
'''
多行注释
多行注释
'''
 
"""
多行注释
多行注释
单引号和双引号作用相同
"""

print('----耀西的分割线--------------------------')

# 打印 print()
print ("Hello, Python!")

# if elif else 缩进空格代表括号（括号一般省略）
# 缩进不一致引发 IndentationError 
if False:
    print ("Answer")
    print ("True")
elif (True):
    print ("123")
else:
    print ("Answer")
    print ("False")    # 缩进不一致，会导致运行错误
print('----耀西的分割线--------------------------')
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('----耀西的分割线--------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('----耀西的分割线--------------------------')
# 同一行可以写多个语句，用；分隔
import sys;x = 'runoob'; sys.stdout.write(x + '\n')
# 交互式显示7，此处的 7 表示字符数，runoob 有 6 个字符，\n 表示一个字符，加起来 7 个字符。

print('----耀西的分割线--------------------------')
# 不换行输出
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('----耀西的分割线--------------------------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

# import 与 from...import
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
from sys import argv,path  #  导入特定的成员
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path