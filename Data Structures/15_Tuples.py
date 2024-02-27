# Without Brackets Python will asume as a tuple

point = (1, 2, 3) + (3, 4) * 3

print(type(point))
print(point[0])
print(point[0:5])
print(point)

if 1 in point:
    print("Exists")
