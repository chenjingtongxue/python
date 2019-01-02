f = open("score.txt")
a=f.read()
L=a.split()
for  i in range(0,len(L)):
	L[i]=int(L[i])
c=[0,0,0,0,0,0]
for x in L:
    if x>=90:
        c[0]+=1
    elif x>=80:
        c[1]+=1
    elif x>=70:
        c[2]+=1
    elif x>=60:
        c[3]+=1
    elif x>=50:
        c[4]+=1
    else:
        c[5]+=1
f.close()#读取完毕
fw=open('scoreresult.txt','w')
s=''
for i in range(9,4,-1):
        s=s+str(i)+'0分以上'+repr(c[9-i])+'\n'
s='成绩统计如下：'+'\n'+s+'50分以下'+repr(c[5])
print(s)
fw.write(s)
fw.close()


                    
