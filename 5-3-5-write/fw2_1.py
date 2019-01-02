L1=[34, 78, 47, 787, 84, 25, 69, 25, 58, 67, 52, 77, 12, 67, 325, 33]
print(len(L1))
f=open('w2-1.txt','w')
for i in range(0,len(L1),2):
    f.write('%s\t%s\n'%(repr(L1[i]),repr(L1[i+1])))
f.close()
