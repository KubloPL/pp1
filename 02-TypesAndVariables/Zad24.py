vehicle_registration = input(
    "Enter vehicle registration number in capital letters: ")

first_two_letters = vehicle_registration[:2]

is_from_krakow = False

if first_two_letters == "KR":
    is_from_krakow = True
elif first_two_letters == "KK":
    is_from_krakow = True
else:
    is_from_krakow = False

print(f"Car from Kraków: {is_from_krakow}")
