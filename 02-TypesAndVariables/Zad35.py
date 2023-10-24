import math

circumference = float(input("Enter tree circumference: "))
can_be_cut_down = False
pi = math.pi

diameter = circumference // (2*pi)


if diameter >= 50:
    can_be_cut_down = True
else:
    can_be_cut_down = False

print(f"Tree can be cut down: {can_be_cut_down}")
