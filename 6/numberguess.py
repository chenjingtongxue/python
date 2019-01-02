num=7
for i in [1,2,3,4,5,6]:
   if i<=5:
      guess=int(input('请输入你猜的数（0～9）：'))
      if guess == num:
         print("恭喜！你猜中了！")
         break
      elif guess > num:
         print("太大,您还有",5-i,'次机会')
      else:
         print("太小,您还有",5-i,'次机会')
         i+=1
   else:   
      print('抱歉，程序结束了')
      
