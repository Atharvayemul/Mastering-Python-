names = ["John", "Mary"]

for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not Found")
# this else block run if the for looop successfuily runs completely
