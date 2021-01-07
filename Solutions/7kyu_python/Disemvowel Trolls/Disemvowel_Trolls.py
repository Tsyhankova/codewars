def disemvowel(string):
    tup = ('a', 'e', 'i', 'o', 'u', 'U', 'A', 'E', 'I', 'O')
    for i in tup:
        if i in string:
            string = string.replace(i, '')
    return string
