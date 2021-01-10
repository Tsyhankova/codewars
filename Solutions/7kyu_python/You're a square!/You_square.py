from math import sqrt
def is_square(n):
    if n >= 0 and sqrt(n) % 1 == 0:
        return True
    else:
        return False
