#参数类型 普通参数 关键字参数 默认参数 收集参数

#收集参数
def tel(*args):
    print("自我介绍：")
    print(type(args))
    for item in args:
        print(item)

#args为list数组,不能使用关键字参数
tel("liuying", 18, "北京大通州区", "wangxiaojing", "single") #普通参数
tel()#默认参数

#收集参数
def my(**kwargs):
    print("自我介绍:")
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,"-"*3, v)
#关键字参数 kwargs 实际为map类型
my(name="yc",age=18,adder="滨江")#关键字参数
my()#收集参数


