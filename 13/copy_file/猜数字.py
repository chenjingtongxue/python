import random
randnum=int(random.uniform(1,10))#光是random.uniform是返回带有小数的随机数
guessnum=int(input('请你猜一个1到10之间的整数:'))
if randnum>guessnum:
    print('您猜小了,随机数是：',randnum)
elif randnum==guessnum:
    print('恭喜，您猜中了')
else:
    print('您猜大了,随机数是：',randnum)
    
