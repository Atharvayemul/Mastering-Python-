
letters = ["a", "b", "c"]

print(letters.index("a"))
print(letters.count('d'))
if "d" in letters:
    print(letters.index("d"))
    # Does not throw error if not found
