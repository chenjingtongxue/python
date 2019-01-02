# Filename: except-division.py
while True:
    try:
        a=float(input('被除数：'))
        b=float(input('除数：'))
        print("%f ÷ %f = %f"%(a,b,a/b))
        break
    except ZeroDivisionError:
        print('小学没读好？除数能为0？')
    except ValueError:
        print('请使用半角的阿拉伯数字！')
    
