# 元组的使用
# 元组定义好之后，不能被修改
tuple1 = (1, 2, 3, '123')
print(tuple1)

# 元组中若只有一个元素，需要加一个‘,’来表示这是一个元组
tupleOne = ('1')
print(type(tupleOne))
tupleTwo = ('1',)
print(type(tupleTwo))

# 强行排序，会自动将tuple的类型转换为list
tuple2 = (1, 2, 3, 0)
change = sorted(tuple2)
print(type(change))

# 元组的方法
# 统计元素的个数
tuple3 = (1, 2, 3, 4, 2, 3, 4)
print(tuple3.count(2))
# 寻找元素的索引值，若元素不存在会报错，所以使用之前要先判断元素存不存在
# 若有多个相同的元素，则返回第一个匹配元素的下标
print(2 in tuple3)
print(tuple3.index(2))


# 返回特定元素的下标，若元素不存在则提示：不存在
userInput = input('请输入想要查找的元素: ')
try:
    userInputInt = int(userInput)
    listReturn = list()
    if userInputInt in tuple3:
        print("元素{}存在{}个".format(userInputInt, tuple3.count(userInputInt)))
        for index, value in enumerate(tuple3):
            if value == userInputInt:
                listReturn.append(index)
        print("下标分别是：", listReturn)
    else:
        print("元素{}不存在于元组中".format(userInputInt))
except ValueError:
    print("请输入数字!")

# 元组遍历
for i in tuple3:
    print(i)
for i, j in enumerate(tuple3):
    print(i, j)
