def descending_order(num):
    a = list(map(int, str(num)))
    a.sort(reverse = True)
    return int(''.join(str(i) for i in a))
