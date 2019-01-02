f=open('word.txt','w')    #如果电脑有这个文件就写进这个文件没有就新建，如果把w换成a就是追加内容
f.write('world')
f.close()   #在进行 写 的操作时一定要关闭文件
f=open('word.txt','a')
f.write('python')
f.close()
