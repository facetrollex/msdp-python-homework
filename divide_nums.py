def divide_nums(a, b):
    if b != 0:
        return a / b
    else:
        print('You cannot divide by 0')
        return None

print(divide_nums(50, 10))
print(divide_nums(50, 0))