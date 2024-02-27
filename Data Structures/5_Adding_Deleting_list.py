
letters = ['a', 'b', 'c']

# ADD
letters.append("d")
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()  # Removes Lst element
letters.pop(2)  # Removes 2 index element
letters.remove('a')  # Remove a element
del letters[0:3]
letters.clear()
print(letters)
