f=open('test.txt','r')    #相对路径，open要有一个返回值f，mode不需要写，若是以读的方式打开可以直接省略'r'
a=f.read()
print(a)
print('文章字符数为：',len(a))
f.close()
