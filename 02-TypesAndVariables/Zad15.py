temp_in_celcius_string = input("Enter temperature in Celcius degrees:")

temp_in_celcius = float(temp_in_celcius_string)

temp_in_kelvin = temp_in_celcius + 273.15
temp_in_fahrenheit = temp_in_celcius * 1.8 + 32

print(f"{temp_in_celcius} in Celcius is {
      temp_in_kelvin} in Kelvin and {temp_in_fahrenheit} in Fahrenheit")
