#Manuel Fernandez
#Task week 6, program ask you for a float number and gives you back an aprox. square root following newton's method
# reference taken about Newton's method: (Calculus/Newton's Method (wikibooks), https://en.wikibooks.org/wiki/Calculus/Newton%27s_Method)
##

# Introduce a number
number =float(input("Please enter a positive number:"))
#function that calculates square roots by powering the number to 0.5
def sqrt(x):
   #define a function to calculate square root applying Newton's method
    # variable n is the aproximate value, is teh result of the derivate of sqaure root
    n=0.5*x 
    # variable m represents the next aproximation value following Newton's method formula
    m= 0.5*(n+(x/n))
    while m != n: #iteration until the two variables get closer (in our case , we will make it equal until the first decimal place. If not keep iterating)
        n=m
        m= 0.5*(n+(x/n))
    return n

#in case the user introduces a negative number, the program will force to introduce
#a positive one.
while number<0:
    number =float(input("You introduced a negative number.Please enter a positive number:"))

#prints the result
print("The square root of",number,"is approx.",round(sqrt(number),1))