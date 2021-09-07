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

#List 操作
a = [1, 2, 3, 4, 5, 6,"aaa"]
a[0] = 9 #針對單個指定元素賦值
print(a)
a[2:5] = [13, 14, 15] #針對
print(a)
a[2:5] = []
print(a)

#Tuple 操作
tup = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tup[0] = 1 tuple的元素無法操作，此處運行會報錯
#string這種操作也會報錯

#Python中 string list tuple都屬於序列，操作方式類似

#由此可看出 string是一種特殊存在的元組

#Set操作 Python中Set表示為集合
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu','Google'}
print(sites) #輸出時，會自動刪除重複的對象

# 成员测试，判斷是否存在
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算，交集、並集、差集
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

#Dictionary key value，
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
print(dict)
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'} #結構
print(tinydict.keys()) #輸出所有key
print(tinydict.values()) #輸出所有value
