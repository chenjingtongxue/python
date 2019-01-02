f=open('list.txt')
a=f.read()
L3=a.split()
print(L3)
print('名称',' '*5,'总金额','\n')
for i in range(0,len(L3)):
    if i%3==0 and i!=0:
        L3[i+1]=int(L3[i+1])
        L3[i+2]=int(L3[i+2])
        s=L3[i]+L3[i+1]*L3[i+2]
        print(s)
f.close
