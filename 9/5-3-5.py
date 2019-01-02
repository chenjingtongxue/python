f = open("score.txt")
a=f.read()
print(a)
L=a.split()
print(L)
for  i in range(0,len(L)):
	L[i]=int(L[i])
print(L)
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
    elif x>=40:
        c[4]+=1
    else:
        c[5]+=1
print("成绩统计结果:")
print("90分以上%d人"%c[0],end=', ')
print("89~80分%d人"%c[1],end=', ')
print("79~70分%d人"%c[2],end=', ')
print("69~60分%d人"%c[3],end=', ')
print("59~40分%d人"%c[4],end=', ')
print("40分以下%d人"%c[5],end='\n')
f.close()

                    
