def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        return sum(n for n in range(begin_number, end_number+1, step))