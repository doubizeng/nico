"""
作者：曾
时间：2017-11-28
备注：今天是一年中的第几天
"""
timeDate = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print("欢迎使用时间计算系统")
year = input("请输入年份：")
month = input("请输入月份：")
day = input("请输入日期：")
if int(year) % 4 == 0 | int(year) % 400 == 0 :
    timeDate[1] = timeDate[1] + 1
    for i in range(int(month)-1) :
        days = timeDate[i] + days
    days = days + int(day)
    print("你好，%s-%s-%s是%s年的第%s天" % (year, month, day, year, days ))
else :
    for i in range(int(month)-1) :
        days = timeDate[i] + days
    days = days + int(day)       
    print("你好，%s-%s-%s是%s年的第%s天" % (year, month, day, year, days ))