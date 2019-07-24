#解包符号使用
def stu(*args):
    print(type(args))
    for item in args:
        print(item)

#stu("yc","YChao",18, 20)

list=["yc","YChao",18, 20]
#list解析要用到解包符号
stu(*list)

def my(**kwargs):
    print("自我介绍:")
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,"-"*3, v)
#关键字参数 kwargs 实际为map类型
yc={"name":"yc","age":18,"adder":"滨江"}#关键字参数
my(**yc)#收集参数


#函数文档'''表示
def stu(name, age):
    '''
    这是文档的文字内容
    :param name: 表示学生的姓名
    :param age: 表示学生的年龄
    :return: 此函数没有返回值
    '''
    pass #该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行


print(help(stu))

print("*" * 20)

print(stu.__doc__)

print(locals())
print(globals())

print(id(list))
del list[1]
print(id(list))
print(list)

#循环列表
a = [["one", 1, "eins"], ["two", 2,"zwei"], ["three", 3,"drei"] ]
for k,v,m in a:
    print(k, "--", v, "--",m)

a=range(0,35)
b=[x for x in a if x%2==0]
print(b)

#链表嵌套
x=[m+n for m in a if m%2!=0 for n in b]
print(x)

print(id(x))
x.insert(4,666)
print(x)
x.pop(4)
print(x)
if 666 in x:
    x.remove(666)#remove不存在时会报错
    print(x)

#reverse 反转数组
x.reverse()
print(x)

#数组拼接
x.extend(b)
