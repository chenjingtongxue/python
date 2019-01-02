f=open('test.txt')
for i in range(0,9):
    a=f.readline()
print(a)
l=a.split(' ')
print(l)
print('本次实验人数：',l[1])
f.close
