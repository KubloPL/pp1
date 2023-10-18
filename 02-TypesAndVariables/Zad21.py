my_height_cm = 190  # cm
my_height_ft = my_height_cm / 30.48
# i remove rounded height in feet from height in feet to get the remainder and multiply by 12 to convert ft to inches
my_height_in = (my_height_ft - int(my_height_ft)) * 12


print(f"I am {my_height_cm} tall, i.e. {
      int(my_height_ft)} feet and {int(my_height_in)} inches.")
