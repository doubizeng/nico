# _*_  utf-8 _*_ 
"""
作者：逗比曾
时间：2017-11-29
描述：函数
"""
def user() :    
    Name = ["Tom", "Zeng", "Harden"]

    People = {
        "Tom": {
            "age": 18,
            "high": 172,
            "sex": "boy"
        },
        "Zeng": {
            "age": 27,
            "high": 170,
            "sex": "boy"
        },
        "Harden": {
            "age": 22,
            "high": 198,
            "sex": "boy"
        }
    }

    for key in Name :
        print("姓名：%s, 年龄：%s,身高: %s,性别：%s" % (key, People[key]["age"],  People[key]["high"], People[key]["sex"]))

def Sum(a, b):
    print(a+b)
Sum(3, 5)    