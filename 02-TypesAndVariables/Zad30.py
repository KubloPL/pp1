import random

random_number = random.randint(1, 6)

is_special = False

if random_number == 6 or random_number == 1:
    is_special = True
else:
    is_special = False

print("Dice rolled: ", random_number)
print("Special number:", is_special)
