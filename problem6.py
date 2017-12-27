def euler6(num):
    
    sum_square = 0
    sum_all = 0
    
    for i in range(1, num + 1):
        sum_square += i ** 2
        sum_all += i
    return sum_all ** 2 - sum_square

print(euler6(100))
