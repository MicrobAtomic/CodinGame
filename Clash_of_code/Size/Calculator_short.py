import math
r=input()
s=input().replace('x','*')
try:
 if r[0]>'n':s=s.translate(str.maketrans("+-*/","-+/*"))
 print(math.ceil(eval(s)))
except:print('Error')