def sum_two_smallest_numbers(numbers):
    min_num = numbers
    min_num.sort(reverse = True)
    first = min_num.pop()
    second = min_num.pop()
    return first + second
