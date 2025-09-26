<<<<<<< HEAD
# Building a Body Mass Index

#convert to floats first
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#BMI calculation
square_height = height ** 2
bmi_calculation = weight/square_height

# Output
print(f"The body mass index is: {bmi_calculation:.3f}")

#Conditions
if bmi_calculation < 18.5:
    print("Underweight")
elif 18.5 <= bmi_calculation <= 24.5:
    print("Normal weight")
elif 25 <= bmi_calculation <= 29.9:
    print("Overweight")
else: 
=======
# Building a Body Mass Index

#convert to floats first
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#BMI calculation
square_height = height ** 2
bmi_calculation = weight/square_height

# Output
print(f"The body mass index is: {bmi_calculation:.3f}")

#Conditions
if bmi_calculation < 18.5:
    print("Underweight")
elif 18.5 <= bmi_calculation <= 24.5:
    print("Normal weight")
elif 25 <= bmi_calculation <= 29.9:
    print("Overweight")
else: 
>>>>>>> 61f03bfc8a79f67cad6e53267ee1026ad9187578
    print("Obesity")