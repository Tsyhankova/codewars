def high_and_low(numbers):
    l = []
    for i in numbers:
        a = numbers.split(' ')
        for j in a:
            j = int(j)
            l.append(j)
            max_j = str(max(l))
            min_j = str(min(l))
    answer = (max_j, min_j)       
    print(' '.join(answer))
    return ' '.join(answer)
