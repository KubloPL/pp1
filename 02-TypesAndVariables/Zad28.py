height_cm = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')

height_m = float(height_cm) / 100

bmi = float(weight) / (height_m * height_m)
is_bmi_correct = False

if bmi >= 18.5 and bmi <= 24.9:
    is_bmi_correct = True
else:
    is_bmi_correct = False

print('Your BMI index: ', bmi)
print('Correct weight: ', is_bmi_correct)
