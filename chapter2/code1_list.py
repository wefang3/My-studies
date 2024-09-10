# 列表的使用,内部可有不同的类型,也可以有相同的值
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, True, True, 1]
list3 = [1, 23]
list4 = []
print(list1)

# 类型转换
# str --> list
a = '123456'
print(list(a))

# 列表的索引
print(list1[0])
# 倒着数
print(list1[-1])

# 列表切片 与 str 差不多
print(list1[1::2])
print(list1[::-2])

# 列表拼接
print(list1 + list2)
print(list1 * 2)

# 列表成员运算
print(0 in list1)

# 内置函数
print(len(list1))

# 若列表中的元素类型不相同，则不能进行计算
# 例子：[1 , 2 ,'3'] 中 str不能与 int进行比较和计算
# True 相当于 1，False 相当于 0 ，因此可以与 int型比较
print(max(list2))
print(min(list1))
del list3
print(sorted(list2))

# 列表遍历
for i in list1:
    print(i, end=' ')
print()
print('-' * 30)
# 包含索引的遍历
for i, j in enumerate(list2):
    print(i, j)

print()
print('-' * 30)

# 常用方法
# 添加元素
list4.append(3)
# 添加列表
list4.extend(['123'])
# 插入元素
list4.insert(1, '456')
print(list4)
# 根据索引删除元素
list4.pop(2)
print(list4)
# 根据值删除元素(有相同的，只会删除索引靠前的元素)
list4.remove(3)
print(list4)
# 寻找元素，返回下标
print(list4.index('456'))

# 排序
list4.append('1')
list4.append('2')
list4.append('0')
list4.append('-9')
# list4.sort() 在原有的列表上进行修改，不会产生新的列表
# sorted(list4) 不会对原有的列表进行修改，而是产生新的列表
list4.sort()
print(list4)

# 列表求和计算
listA = [20, 50, 67, 48, 96]
b = 0
for i in listA:
    b += i
print("{:.3f}".format(b / len(listA)))

# 简便方法
print(sum(listA) / len(listA))
