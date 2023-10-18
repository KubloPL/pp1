number = input("Enter number: ")
is_in_range = False

if int(number) <= 10 and int(number) >= -10:
    is_in_range = True
else:
    is_in_range = False

print(f"Number in te range <-10, 10>: {is_in_range}")
