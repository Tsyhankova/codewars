def is_isogram(string):
    string = string.lower()
    if len(string) == 0:
        return True
    else:
        return len([i for i in string if string.count(i) > 1]) == 0
