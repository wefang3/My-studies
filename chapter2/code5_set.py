# 集合的使用
# set定义
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# 空set，不能用 {}，这表示一个字典
set2 = set()
set3 = {12, 2, 3, 6, 0}
print(set1)
print(set2)
print(set3)
print()
print('-' * 30)

# 交集，并集
# 交集
print(set1 & set3)
print(set1 | set3)

list1 = [70, 92, 70, 90, 20, 20, 20]
setList = set(list1)
map1 = dict()
for i in setList:
    t = list1.count(i)
    map1[i] = t
    print("得分为{}的人有{}个".format(i, t))
print(map1)
