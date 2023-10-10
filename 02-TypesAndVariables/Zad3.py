hours_string = input("Enter hours: ")
rate_string = input("Enter rate: ")

hours = float(hours_string)
rate = float(rate_string)

pay = hours*rate

print("Pay: " + str(pay))