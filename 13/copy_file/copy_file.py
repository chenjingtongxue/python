import os
sname=input("输入原文件名:")
dname=input('输入目标文件名：')
copy=True
if not os.path.exists(sname):
    print('原文件不存在')
    copy=False
elif os.path.exists(dname):
    answ=input('目标文件已存在，是否覆盖该文件？(Y/N)')
    if not( answ=='y' or answ=='Y'):
        copy=False
if copy:#相当于copy==Ture
    fs=open(sname,'r')
    a=fs.read()
    fd=open(dname,'w')
    fd.write(a)
    fs.close()
    fd.close()
    print('文件复制成功!')
