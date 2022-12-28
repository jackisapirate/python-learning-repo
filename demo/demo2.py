# 2.1单行注释和多行注释
print("# 2.1单行注释和多行注释")
'''
多行注释1
'''
"""
多行注释2
"""
# 2.2变量
print("# 2.2变量")
# 变量无需声明即可赋值
a=20
print(a)
# python 是弱类型语言，可以给同一变量不同类型的赋值
a="Hello World"
print(a)
print(type(a)) # type()可以查看变量类型

# 使用print输出内容到屏幕，多个字符和变量用'空格'分割
user_name = 'Charlie'
user_age = 8
print("His name is", user_name, "age is", user_age)
print("His name is", user_name, "age is", user_age, sep='|') # 指定分割符号
print("His name is", user_name, "age is", user_age, sep="-") # 指定分割符号
# 利用end="" 终止print换行
print(50, '\t', end="")
print(60, '\t', end="")
print(70, '\t', end="")
# 将内容输出到文件
f = open("poem.txt", "w")
print("锄禾日当午", file=f)
print("吃块烤白薯", file=f)
f.close()
# 关键字 导入关键词模块
import keyword
print(keyword.kwlist)

# 2.3数值类型
print("# 2.3数值类型")
# 整型
a = 5
print(type(a))
a = 99999999999999999999999999999999
print(type(a)) # 还是int，如果python2.x会显示long 且大整型不会溢出
# 整型支持None
a = None
print(a) # None
print(type(a)) #NoneType

# 浮点型
af1 = 5.5556677
print("浮点型的类型为：", type(af1))
af2 = 5e4 # 50000.0 科学计数法
print(af2)
print("浮点型的类型为：", type(af2))

# 2.4字符串
print("# 2.4字符串")
# 声明两个字符串会自动拼接 或者 也可以用+拼接
s1 = "Hello"    'World'
print(s1) # HelloWorld 
# 字符串拼接其他类型会报错，需要用str()转换
p = 88.9
print(s1 + str(p))
print(repr(s1)) # repr()会自动在类型外包裹一层引号
print(repr(repr(repr(s1))))
