# 单行注释1
print("abc")  # 单行注释2

'''
多行注释
'''

"""
多行注释
"""

if True:
    print("true")
else:
    print("false")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
 # print ("False")    # 缩进不一致，会导致运行错误

# 变量声明，前面不能有空格
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
#a = b = c = 1
a, b, c = 1, 2, "runoob"
print(a,b,c)
print(type(a), type(b), type(c)) #type 获取变量类型
if isinstance(a,int):
    print("a是整数")

strvalue = '123456789'
print(strvalue)                 # 输出字符串
print(strvalue[0:-1])           # 输出第一个到倒数第二个的所有字符
print(strvalue[0])              # 输出字符串第一个字符
print(strvalue[2:5])            # 输出从第三个开始到第五个的字符
print(strvalue[2:])             # 输出从第三个开始后的所有字符
print(strvalue[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(strvalue * 2)             # 输出字符串两次
print(strvalue + '你好')         # 连接字符串

# 加减乘除运算
a = 1
b = 2
print(a+b)
print(a/b)
print(a-b)
print(a*b)

# 一行多条语句
print("一行多条语句")
print("一行多条语句")

# 字符串拼接
result = 1
# print("输出"+1) python中盖写法会报错，字符串无法直接拼接int类型
if result == 1:
    print("输出" + str(1))
elif result == 2:
    print("输出"+str(2))
else:
    print("输出"+str(2))

#引入sys模块
import sys
#引入sys模块的部分成员，多个用逗号隔开
from sys import argv,path

for i in sys.argv: #循环
    print(i)

print(issubclass(bool, int) ); #python中 bool为int类型的子类
print(True==1);print(False==0) # 即True = 1 ，false = 0
print(True+False) # 同理 TRUE和FALSE是可以做数学运算的

var1 = 1
var2 = 2
del var1 # 删除了var1这个变量，print(var1)时则报错
#del var1,var2 #已经删除的变量无法重复删除
