letter,digit,space=0,0,0
def count(n):
    global letter,digit,space#如果没有global这句话，主程序还是会屏蔽全局变量在函数里的操作
    #global是声明
    for i in range(len(n)):
        if n[i].lower()>='a' and n[i].lower()<='z':
            letter+=1
        if n[i]>='0' and n[i]<='9':
            digit+=1
        if n[i]==' ' :
            space+=1                
str1=input('please input string:')
count(str1)
print('总计%d个字母，%d个数字，%d个空格'%(letter,digit,space))
