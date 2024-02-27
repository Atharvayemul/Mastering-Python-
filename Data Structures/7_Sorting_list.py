
numbers = [2, 23, 43, 5, 654, 34]

# numbers.sort(reverse=False)

# Sorted function creates new array does not modify original one
print(sorted(numbers))

print(numbers)

items = [
    ("Product", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=lambda item: item[1])
print(items)
