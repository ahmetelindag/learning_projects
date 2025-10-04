# Profile Creator
# Created by Ahmet

print("Welcome! Let's create your profile.\n")

# User input
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
job = input("Enter your job: ")
studentCheck = input("Are you a student? (yes/no): ")
studentStatus = True if studentCheck.lower() == 'yes' else False

# Calculations
bmi = weight / (height ** 2)

# Display profile
print("\nProfile Information:")
print("--------------------------------")
print("Name: " + name.upper())
print("Age: " + age)
print("City: " + city)
print("Height: " + str(height) + " m")
print("Weight: " + str(weight) + " kg")
print("Job: " + job)
print("BMI: " + str(round(bmi, 2)))
print("Student Status: " + ("Yes" if studentStatus else "No"))
print("--------------------------------\n")

print("Thank you for using our profile creator!")
