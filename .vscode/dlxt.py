for i in range(4) :
    if i != 3 :
        print("------------------------------")
        print("|----------------------------|")
        print("|----------xx登录系统---------|")
        print("|----------------------------|")
        print("------------------------------")
        username = input("请输入用户名")
        if username == "zengyouwei" :
            usercode = input("请输入密码")
            if usercode == "qwe721213" :
                print("登录成功")
            else :
                print("密码错误")
    else :
        print("用户名不存在")        
else :
    print("连续三次密码输入，请确认密码")