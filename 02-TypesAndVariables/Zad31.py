import random

random_number = random.randint(1, 6)
entered_number = int(input("Enter a number between 1 and 6: "))

if entered_number == random_number:
    print("You won!")
else:
    print("You lost! The number was " + str(random_number) + ".")
