# return the sum of the two polynomials p1 and p2.  
from math import fabs
def poly_add(p1, p2):
    if len(p1) == len(p2):
        a = list(map(lambda x, y: x+y, p1, p2))
    elif len(p1) > len(p2):
        m = int(fabs(len(p1)-len(p2)))
        a = list(map(lambda x, y: x+y, p1, p2)) + list(p1)[-m:]
    else:
        m = int(fabs(len(p1)-len(p2)))
        a = list(map(lambda x, y: x+y, p1, p2)) + list(p2)[-m:]
    return  a 
