# 私有变量案例

class PrivatePerson():
    # name是共有的成员
    name = "liuying"
    # __age就是私有成员
    __age = 18
    def __init__(self):
        self.name=""
        self.address="homeTown"


p = PrivatePerson()
# name是公有变量
print(p.name)
# __age是私有变量
print(p._PrivatePerson__age)
print(p.address)

# name mangling技术
print(PrivatePerson.__dict__)

p._PrivatePerson__age = 19

print(p._PrivatePerson__age)


#派生类和基类取相同的名字就可以使用基类的私有变量
class A():
    def __init__(self):
        self.__name = 'python'  # 翻译成self._A__name='python'

class B(A):
    def func(self):
        print
        self.__name  # 翻译成print self._B__name

instance = B()
# instance.func()#报错：AttributeError: B instance has no attribute '_B__name'
print(instance.__dict__)
print(instance._A__name)
