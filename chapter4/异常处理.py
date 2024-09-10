try:
    year = input("请输入年份: \n")
    year = int(year)
    if year < 1900:
        # 手动抛出异常，throw
        raise Exception("年份太小啦！")
    if 1900 <= year <= 2100:
        raise Exception("年份还是小！")
except ValueError as e:
    print("请输入数字！")
    print("报错信息为：", e)
except Exception as e:
    print(e)
# 没有异常走这边
else:
    if (not year % 4 and year % 100) or (not year % 400):
        print('闰年')
    else:
        print('非闰年')
finally:
    print("无论如何都会进入finally")
