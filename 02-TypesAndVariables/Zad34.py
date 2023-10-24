speed = int(input("Enter vehicle speed: "))
is_correct = False

if speed >= 40 and speed <= 140:
    is_correct = True
else:
    is_correct = False

print(f"Speed is valid: {is_correct}")
