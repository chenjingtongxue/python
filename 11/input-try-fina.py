n=0
while True:
    n+=1
    try:
        a=int(input('plaease insert a munber:'))
    except ValueError:
        print('请输入阿拉伯数字!')
    else:
        if a>10:
            print('ok')
        else:
            print('no')
    finally:
        print('你还有%d次机会'%(5-n))
        if n==5:
            break
    
