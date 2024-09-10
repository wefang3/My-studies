# 字符串的使用

words = '1234567'

# 获取第一个(头从 0 开始)
print(words[0])
# 获取最后一个(尾从 -1 开始)
print(words[-1])
# 获取中间的
print(words[int(len(words) / 2)])

# 字符串截取
# s[start,end,step] (包前 : 不包后 : 步数);
# 若 start与 end大于字符串长度，不会报错
print(words[6:7])
# 从头开始截取
print(words[:4])
# 从start开始截取，到最后结束
print(words[1:])
# 每隔2个进行截取
print(words[::3])

# 字符串反转(要倒着数,从 -1 开始)
print(words[-1:-8:-1])
# 简化
print(words[::-1])
# 取中间位置，反转
print(words[-2:-7:-1])

# 字符串方法[查文档吧]
# 如果字符串只包含数字则返回 True 否则返回 False。
print(words.isdigit())
ww = " lk lk 09"
print(ww.replace(" ", ""))

print()
print('-' * 20)

# 字符串用法
str1 = '1234'

# 获取元素
print(str1[0])
# 多次打印
print(str1 * 2)
# 长度
print(len(str1))
# 最大最小比大小，比较ASCII码值
print(max(str1), min(str1), 'acc' < 'b22')
# in
print('s' in str1)
