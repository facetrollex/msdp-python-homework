def divisible_in_range(start, end):
    foundNumber = []
    for num in range(start, end+1):
        if num % 7 == 0 and num % 5 != 0:
            foundNumber.append(num)
    return foundNumber        

print(divisible_in_range(0, 77))