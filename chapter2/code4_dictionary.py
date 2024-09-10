# 字典的用法(map),无序
# 字典定义
map1 = {"name": "123",
        "age": 12,
        "height": 22}
# 空字典
map2 = {}
map3 = dict()

map4 = {"name": "123",
        "age": 12,
        "height": 22}

# 新增
map1["big"] = 'pp'
print(map1)
# 删除单个元素
map1.pop("big")
print(map1)
# 删除所有元素
map1.clear()
print(map1)

# 字典遍历
for i in map4:
    print(i, map4[i])

for k, v in map4.items():
    print(k, v)