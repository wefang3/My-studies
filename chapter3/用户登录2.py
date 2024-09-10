# 用户信息2
userMsg = {
    'qqq': {"name": "qqq", "password": "123", "isBlackUser": True, "loginCount": 0},
    'www': {"name": "www", "password": "123", "isBlackUser": False, "loginCount": 0},
    'eee': {"name": "eee", "password": "123", "isBlackUser": False, "loginCount": 0},
    'rrr': {"name": "rrr", "password": "123", "isBlackUser": False, "loginCount": 0},
    'ttt': {"name": "ttt", "password": "123", "isBlackUser": False, "loginCount": 0}
}

while True:
    userName = input('请输入用户名：')
    userPwd = input('请输入密码：')
    if userName in userMsg.keys():
        # 获取到用户信息
        userInfo = userMsg[userName]
        # 校验尝试登录次数
        if userInfo['loginCount'] >= 3:
            print('用户尝试登录次数已达上限，请联系管理员处理！')
        else:
            # 校验密码和是否在黑名单中
            if userPwd == userInfo['password'] and not userInfo['isBlackUser']:
                print('登录成功')
                break
            elif userPwd == userInfo['password'] and userInfo['isBlackUser']:
                print('用户被限制，无法登录')
            else:
                print('密码错误')
                # 尝试登录次数+1
                userInfo['loginCount'] += 1
    else:
        print('用户不存在')
