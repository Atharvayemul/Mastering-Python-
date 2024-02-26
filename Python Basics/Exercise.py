def fizz_buzz(input):
    if input % 3 and input % 5:
        return "FizzBuzz"
    elif input % 3:
        return "Fizz"
    elif input % 5:
        return "Buzz"
    else:
        return input


print(fizz_buzz(30))
