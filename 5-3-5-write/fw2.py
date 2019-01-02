L1=[34, 78, 47, 787, 84, 25, 69, 25, 58, 67, 52, 77, 12, 67, 325, 33]
f=open('w2.txt','w')
for i in L1:
    f.write(repr(i)+'\n')
f.close()
