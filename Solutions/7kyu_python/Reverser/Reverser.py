def reverse(n):
    q = 0
    while n > 0:
        reminder = (n % 10)
        q = (q*10) + reminder
        n = n//10
    return q
