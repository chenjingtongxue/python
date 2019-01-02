f=list(open("list.txt"))
L3=[]
for line in f[1:len(f)]:
    print(line)
    line=line.strip()#去除行首尾的空白
    L1=line.split()
    f_add=int(L1[1])*int(L1[2])
    print(f_add)
    L3.append([L1[0],f_add])
print(f)

f2=open("total.txt",'w')
f2.write("名称\t总金额\n")
n=0
for L2 in L3:
    f2.write(L2[0]+'\t'+str(L2[1])+"\n")
    if L2[1]>=30:
        n+=1
f2.write('总金额大于等于30的商品有%d种'%n)    
f2.close()

