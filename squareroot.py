#Task week 6, program ask you for a float number and gives you back an aprox.

# Introduce a number
number =float(input("Please enter a positive number:"))
#function that calculates square roots by powering the number to 0.5
def sqrt(x):
    return x**(0.5)

print("The square root of",number,"is approx.",round(sqrt(number),1))