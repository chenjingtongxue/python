import datetime
while True:
    yourAge = int(input('输入你的年龄 --> '))
    if yourAge<0:
        print("请输入一个大于等于0的整数！")
        continue
    print('你的年龄是 %d 岁，你生于 %d 年'%(yourAge,datetime.date.today().year-yourAge))
    break
print('加油!')
