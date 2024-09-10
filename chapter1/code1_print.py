# 单行注释
# print的用法

year, month, day = 2024, 2, 20

# print 参数定义
# print(self, *args, sep=' ', end='\n', file=None)
# 1.如果不指定 sep，默认为 空格作为分隔符, end 作为结束后的补充添加，默认为换一行。
print(year, ",你好(default sep,default end)")
print(year, ",你好(change sep,change end)", sep='', end='\n\n')

# 2.print 以逗号作为拼接标识，可拼接多组数据。
print("nextLine to show:", 2, [123, "13"], {2, 3, 4})

# 3.print %占位符使用
# %02d 不足两位时，自动用 0 补充两位
print("%d年 %02d月 %d日" % (year, month, day))
# 建议使用以下两种方式,更简洁
# f-string 方式
print(f"{year}年 {month:02}月 {day}日")
# .format() 方式
print("{}年 {:02}月 {}日".format(year, month, day))

# 补充
# 1.变量的创建
num1 = num2 = num3 = 5  # 可进行连等赋值
a, b, c = 1, 2, '123'  # 可进行不同赋值

# 2.python 中变量的数据类型可进行修改，因此直接修改变量即可。
# 3.python 中没有专门的常量类型，因此一般用大写标识常量。
# 4.使用type()检查数据类型。
# 数据类型【int，float，double，str，boolean，List，Tuple（元组），Set，Dictionary（字典map）】
# 简单数据类型不必解释，复杂数据类型，后面解释。

str0 = 'yuppy'
print("str0的类型是：", type(str0))
