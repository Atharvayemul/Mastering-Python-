numbers = {1, 1, 2, 3, 4}

uniques = set(numbers)

second = {1, 4, 1}
second.add(5)
second.remove(5)
len(second)

print(second)


print(numbers | second)  # Union

print(numbers & second)  # Interesction

print(numbers - second)
print(numbers ^ second)

if 1 in numbers:
    print("Exists")
