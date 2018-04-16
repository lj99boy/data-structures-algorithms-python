import re
import os

def sumInt(fname):
    # re_int = r'\b([+-]?0|[1-9]\d*\b)'
    re_int = r'([+-]?0|[1-9]\d*)'
    inf = open(fname)
    if inf == None:
        return 0
    int_list = map(int,re.findall(re_int,inf.read()))
    s = 0
    for value in int_list:
        s = s + value
    return s

fname = os.path.join(os.path.dirname(__file__),'testFile')

# print(fname)
print(sumInt(fname))

