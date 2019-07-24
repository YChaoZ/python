# 收集参数混合调用案例
# stu模拟一个学生的自我介绍
def stu(name, age, *args, hobby="没有", **kwargs):
    print("Hello 大家好")
    print("我叫 {0}， 我今年{1}大了。".format(name, age))
    if hobby == "没有":
        print("我没有爱好， so sorry")
    else:
        print("我的爱好是{0}".format(hobby))

    print("*" * 20)

    for i in args:
        print(i)

    print("#" * 30)

    for k, v in kwargs.items():
        print(k, "---", v)


# 开始调用函数
name = "liuying"
age = 19

# 调用的不同格式
stu(name, age)

stu(name, age, hobby="游泳")

stu(name, age, "王晓静", "刘石头", hobby="游泳", hobby2="烹饪", hobby3="跟不同女生聊天")