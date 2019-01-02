while True:
    try:
        a=int(input('plaease insert a munber:'))
    except ValueError:
        print('请输入阿拉伯数字!')
    else:
        if a>10:
            print('ok')
        else:
            print('no')
    
