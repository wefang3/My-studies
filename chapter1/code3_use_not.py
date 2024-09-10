# not 的用法

# 1.not 是逻辑判断词，用于布尔型 True和False ，not+True 为 False，not+False 为True
# 例1：
a = False
b = True
print("例子1：not a = ", not a, ",not b = ", not b, sep='')

# 2.可用于判断元素是否在列表或者字典中
a = 5
b = [1, 2, 3]
print("例子2：", a not in b, sep='')  # 返回True，a 不在 b 中

# 3.在 python 中 None, False, 空字符串 "", 0, 空列表[], 空字典{}, 空元组()都相当于 False
# 因此在判空的时候需要注意 [] 与 None 的区别
x = [2]
y = None
print("例子3：not x = ", not x, ",not y = ", not y, sep='')
# 判空操作，先判断非None，在判断非空
if x is None:  # 此处先判断是否为 None
    print("x is None")
elif not x:  # 此处判断是否为 空列表
    print("x is Empty")
else:
    print(x[0])

# 简化
if x is None or not x:
    print("x is None" if x is None else "x is Empty")
else:
    print(x[0])

# 相同，进行反向
if x is not None and x:
    print(x[0])
else:
    print("x is None" if x is None else "x is Empty")


# 4.补充 is None 与 == None 的区别
# 若 变量为 函数的话 有区别
class Foo:
    # 重写 eq() 函数
    def __eq__(self, other):
        return True


f = Foo
print(f == None)  # 此处会调用 eq 函数，而我们重写了eq 函数，所以只会返回 True
print(f is None)  # 此处是真正的判断 None

# 5.补充 两个对象之间的判断
o = [1]
p = [1]
print("o == p:", o == p)
print("o is p:", o is p)
