num=7
for i in range(5,0,-1):
    guess=int(input('请输入你猜的数（0～9）：'))
    if guess == num:
        print("恭喜！你猜中了！")
        break
    elif guess > num:
        print("太大,您还有",i-1,"次机会")
    else:
        print("太小，您还有",i-1,"次机会")
print("抱歉，程序结束了")        
              
