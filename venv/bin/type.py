para = (1,2,3)

print(type(para))
#类型转换 list
l_para=list(para);
print(list(para))

print(type(l_para))
#list从0开始
print(l_para[1])
#截取字符包左不包右 : : 1 默认增幅1
print(l_para[:])

print(l_para[::2])

l = [3,2,1,4,6,3,2]
# 分片之负数下标
print(l)
# 下面显示的是为空，因为默认分片总是从左向右截取
# 即正常情况，分片左边的值一定小于右边的值
print(l[-2:-4])
print(l[-4:-2])
# 如果分片一定左边值比右边大，则步长参数需要使用负数
# 此案例为一个list直接正反颠倒提供了一种思路
print(l[-2:-4:-1])
