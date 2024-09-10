# 函数的定义

# num2=0 表示默认值，缺省参数
def a(num1, num2=0):
    print('this is a')
    return int(num1) + int(num2)


r = a(1, 2)
s = a(4)
print(r)
print(s)


def b(num1, num2=0, num3=0):
    print('this is a')
    return int(num1) + int(num2) + int(num3)


# 此处为默认值传值
print(b(4, num3=2))
