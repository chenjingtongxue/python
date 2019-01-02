f=open('data3.txt')
a=f.read()
l=a.split()#这里已经转换成字符串了，所以后面不用在转换
f.close()
fout=open('out.txt','w')
s=''
for i in range(len(l)):
    s=s+l[i]+'\t'
    if (i+1)%5==0:
        s=s+'\n'
fout.write(s)
fout.close()

    
