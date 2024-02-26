# Python Function always returns None
# In Python we can also return Multiple values


def increment(number: int, by: int) -> tuple:
    return (number, number + by)


print(increment(number=2, by=3))
