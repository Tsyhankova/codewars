def find_short(s):
    list_len = []
    for word in s.split(' '):
        list_len.append((len(str(word))))
    min_str = min(list_len)
    return min_str # shortest word length
