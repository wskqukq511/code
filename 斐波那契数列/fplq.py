#迭代实现
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("输入有误!")
        return -1
    while (n - 2) > 0 :
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3
result = fab(20)
if result != -1:
    print("共有%d对小名兔崽子诞生！" % result)



#递归实现
def fab(n):
    if n < 1:
        print("输入有误!")
        return -1

    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
result = fab(20)
if result != -1:
    print("共有%d对小名兔崽子诞生！" % result)