import math
def CalArea(a,b,c):
     s=(a+b+c)/2.0
     area=math.sqrt(s*(s-a)*(s-b)*(s-c))
     return area
