# Two Ways of Defining a Dicionary
point = {
    "x": 1,
    "y": 2
}
point = dict(x=1, y=4)

if "a" in point:
    print(point["a"])

print(point.get("a", 0))
# Get function returns 0 if not found a

del point["x"]

print(point)

for key in point:
    print(key, point[key])

for key, values in point.items():
    print(key, values)
