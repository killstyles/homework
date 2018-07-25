'''
字典推导式
两个列表组合
'''
import itertools

a = [0,1,2,3,4]
b = [0]
c = list(itertools.product(a,b))
print(c)
d = {k:v for (k,v) in c}
print(d)
