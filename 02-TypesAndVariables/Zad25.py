age_str = input("Enter age: ")
exemption = False
age = int(age_str)

if age <= 26:
    exemption = True
else:
    exemption = False

print("Exemption from paying taxes: " + str(exemption))
