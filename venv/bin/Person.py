class Person():
    name=""
    age=18
    __addr="henan"
    def __init__(self,name,age):
        print("Person 初始化, {},{}".format(name,age))
        #self和__class__获取为类内属性
        print("Person 初始化, {},{}".format(self.name,self.age))
        print("Person 初始化, {},{}".format(__class__.name, __class__.age))
        print("*"*20)

    def say_hi(self):
        self.name="zzzz"
        self.age="48"
        print("我叫{},年纪是{}".format(self.name,self.age))
        print("我叫{},年纪是{}".format(self.name, self.age))
        print("*" * 20)

# 初始化类，self会优先传入y值，即self为占位符
y = Person("yc",28)

# y.name="YChao"
# y.age="38"
# print(y.__dict__)
# print(Person.__dict__)

y.say_hi()

print(y.__addr)