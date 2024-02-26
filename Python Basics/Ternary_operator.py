age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligibile"

# message = age >= 18 ? "Elibile" : "Not Eligible"

message = "Eligible" if age >= 18 else "Not Eligible"

print(message)
