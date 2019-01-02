f=open("test.txt")
a=f.readlines()#a是个列表
str1=a[-2].split()
print(str1)#split用完返回一个列表，即str1为列表
print('本次实验人数是:',str1[1])
f.close()
