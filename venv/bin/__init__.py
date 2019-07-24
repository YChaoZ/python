# 定义一个函数，打印一行九九乘法表
def printLine(row):
    for col in range(1, row + 1):
        # print函数默认任务打印完毕后换行
        print(row * col, end=" ")
    print("")


# 九九乘法表
# version 2.0
for row in range(1, 10):
    printLine(row)

def stu( *args):
    print("Hello 大家好，我自我介绍以下，简答说两句：")
    # type函数作用是检测变量的类型
    print(type(args))
    for item in args:
        print(item)


stu("liuying", 18, "北京大通州区", "wangxiaojing", "single")

stu("周大神")

