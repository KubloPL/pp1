number = input("Enter a number: ")
number = int(number)
is_even = False

if number % 2 == 0:
    is_even = True
else:
    is_even = False

print(f"Number is even: {is_even}")
