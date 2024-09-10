# 用户信息1
userMsg = [
    {"name": "qqq", "password": "123", "isBlackUser": True, "loginCount": 0},
    {"name": "www", "password": "123", "isBlackUser": False, "loginCount": 0},
    {"name": "eee", "password": "123", "isBlackUser": False, "loginCount": 0},
    {"name": "rrr", "password": "123", "isBlackUser": False, "loginCount": 0},
    {"name": "ttt", "password": "123", "isBlackUser": False, "loginCount": 0}
]

flag = True
while flag:
    userName = input('请输入用户名：')
    pwd = input('请输入密码：')
    for user in userMsg:
        if userName == user['name']:
            if user['loginCount'] >= 3:
                print('用户尝试登录次数已达上限，请联系管理员处理！')
            else:
                if pwd == user['password']:
                    if not user['isBlackUser']:
                        print('登录成功')
                        flag = False
                        break
                    else:
                        print('用户被限制，无法登录')
                else:
                    print('密码错误')
                    user['loginCount'] += 1
            break
    else:
        print('用户不存在')
