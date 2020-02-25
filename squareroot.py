#Task week 6, program ask you for a float number and gives you back an aprox.

# Introduce a number
number =float(input("Please enter a positive number:"))
#function that calculates square roots by powering the number to 0.5
def sqrt(x):
    return x**(0.5)

#in case the user introduces a negative number, the program will force to introduce
#a positive one.
while number<0:
    number =float(input("You introduced a negative number.Please enter a positive number:"))

#prints the result
print("The square root of",number,"is approx.",round(sqrt(number),1))