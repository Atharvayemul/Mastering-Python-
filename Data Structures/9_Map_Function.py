items = [
    ("Product", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []

for item in items:
    prices.append(item[1])

# Instead of this we can write map function
# map(function,iterables)
# The map function will apply function to each iterable and create new list

x = list(map(lambda item: item[1], items))
print(x)
print(prices)
