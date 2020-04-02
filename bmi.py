# Manuel Fernandez
# Script that calculates the Body Mass Index (BMI)
# dividing the weight by the hight in metres square

# Definition of the variables introduced by the user

Weight = float(input("Enter weight (in Kg)"))
Height = float(input("Enter Height (in cm)"))*0.01

# BMI formula

bmi = Weight/((Height*Height))

#Print result
print ("BMI is",round(bmi,2))