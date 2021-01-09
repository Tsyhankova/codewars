def accum(s):
    l = 0
    k = []
    for i in s:
        j = i.upper()
        k.append(j + i.lower() * l)
        l+=1
    return "-".join(k)
