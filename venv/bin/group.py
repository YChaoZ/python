#元组切片 切片后为新数据，id不同，
# 起始位置：结束位置：间隔
# 元组数据不能改变，有序，类型不限
t = (1,2,3,4,5,6)
t1 = t[1::2]
print(id(t))
print(id(t1))
print(t1)

# 切片可以超标
t2 = t[2:100]
print(t2)

#元组不能修改是元素不能修改，但可以修改整个元组信息（重新生成新元组）
t1=t1+t2
print(t1)
print(id(t1))

# 元组遍历，一般采用for
# 1. 单层元组遍历
t = (1,2,3,"wangxiaojing", "i", "love")
for i in t:
    print(i, end=" ")

t = ((1,2,3), (2,3,4),("i", "love", "wangxiaojing"))
for i in t:
    print(i)

for k,v,m in t:
    print(k,"----",v,"------",m)

# copy:拷贝
# remove:移除制定的值，直接改变原有值，如果要删除的值不存在，报错
# discard:移除集合中指定的值，跟remove一样，但是删除的话，不报错
# 集合函数
# intersection: 交集
# difference:差集
# union: 并集
# issubset: 检查一个集合是否为另一个子集
# issuperset: 检查一个集合是否为另一个超集
arry = [1,2,3,4]
arry.remove(2) #数组只有remove
arry.pop() #移除指定位置
print(arry)
arry1 = arry.copy()
set = {1,2,3,4,5,6,7}
set.remove(2)
set.discard(4)
print(set)
set.pop() #集合类型时，pop为随机弹出一个参数
print(set)

print(len(arry))

d = {"one": 1, "two": 2, "three": 3}

if 2 in d:
    print("value")

if "two" in d:
    print("key")

if ("two", 2) in d:
    print("kv")
for k,v in d.items():
    print(k,"----",v)

print(type(d))
map = {k:v for k,v in d.items() if v%2==0}
print(map)

d = {"one":1, "two":2, "three":3}
i = d.items()
print(type(i))
print(i)

