f=open('data3.txt','r')
L=[]
a=f.read()
L=a.split()
f.close()
print(len(L))
f=open('data3五列输出.txt','w')
s=''
for i in range(len(L)):
    s=s+str(L[i])+'\t'
    if (i+1)%5==0:
        s=s+'\n'
print(str(s))
f.write(s)
f.close()
