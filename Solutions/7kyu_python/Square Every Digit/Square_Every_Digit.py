def square_digits(num):
    b = str(num)
    l = []
    for i in b:
        j = str((int(i)*int(i)))
        l.append(j)
    return int(''.join(l))
