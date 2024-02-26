
def multiply(*num):
    total = 1
    for number in num:
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))
