def sum_of_nums(i):
    if i == 0:
        return 0
    return i + sum_of_nums(i-1)
print(sum_of_nums(5))