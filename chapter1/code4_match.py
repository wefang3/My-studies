# match(python 3.10 以后支持) 与 java 中的 switch 语句差不多
# match 匹配了其中一个case 之后就不会匹配其他的case了，

# match没有穿透性，执行完具体的 case 中的代码，也不会继续往下执行，直接跳出。
x = 10
match x:
    case 10:
        print('x is 10')
    case 20:
        print('x is 20')
    case _:  # 匹配所有值
        print('other')
