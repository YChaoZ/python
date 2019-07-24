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