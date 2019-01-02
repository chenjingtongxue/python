def count(n):
    letter,digit,space=0,0,0
    for i in range(len(n)):
        if n[i].lower()>='a' and n[i].lower()<='z':
            letter+=1
        if n[i]>='0' and n[i]<='9':
            digit+=1
        if n[i]==' ' :
            space+=1
    print('总计%d个字母，%d个数字，%d个空格'%(letter,digit,space))            
str1=input('please input string:')
count(str1)
#局部变量无法传递在主程序里，所以print那句不能在外面
