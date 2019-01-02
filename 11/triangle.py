import math
a=int(input('直角边长度：'))
c=int(input('斜边长度：'))
print('直角边长度为 %d，斜边长度为 %d'%(a,c))
print('第二条直角边长度为： %f'%math.sqrt(c**2-a**2))
