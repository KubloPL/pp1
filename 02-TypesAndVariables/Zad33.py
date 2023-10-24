password = input("Enter password: ")
is_valid = False

if len(password) >= 8:
    is_valid = True
else:
    is_valid = False

print("Password is valid:", is_valid)
