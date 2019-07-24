def han_no_ta(count,a,b,c):
    '''
    汉诺塔的递归实现
    :param count: 初始数量
    :param a: 起始位置
    :param b: 借助位置
    :param c: 最终位置
    :return:
    '''
    if count==1:
        print(a,"----->",c)
        return None
    '''
    非1数量移动步骤,a经过c移向b
    '''
    han_no_ta(count-1,a,c,b)#每一次中间步骤上一步都是通过a-c-b
    print(a,"----->",c)#中间不中最大盘直接从a-c
    han_no_ta(count-1,b,a,c)#下一步则是由b-a-c


a="A"
b="B"
c="C"
han_no_ta(2,a,b,c)