
# Works similar to the Map Functoin

items = [
    ("Product", 10),
    ("Product2", 9),
    ("Product3", 12),
]


x = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered_ease = [item for item in items if item[1] >= 10]

print(prices)
print(x)

print(filtered)
print(filtered_ease)
