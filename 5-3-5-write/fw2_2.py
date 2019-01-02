L1=[34, 78, 47, 787, 84, 25, 69, 25, 58, 67, 52, 77, 12, 67, 325, 33]
#print(len(L1))
f=open('w2-2.txt','w')
s=''
for i in range(len(L1)):
    s=s+str(L1[i])+'\t'
    if (i+1)%2==0:
        s=s+'\n'
print(repr(s))        
f.write(s)
f.close()
