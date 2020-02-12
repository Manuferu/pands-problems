#program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program end if the current value is one.

#ask user to insert an integer number

p = int(input("Please enter a positive integer:"))
isinteger=False
m = 2

while p >1: # Keep in the loop in the case that always you have a value greater than 1
    if (p % m)==0 : # If the value is even, the reminder will be 0, then enter here 
       p= int(p / 2) #update the value of p dividing by 2
        
    else: # if the reminder is not 0, then is odd, enter here
        p = (p * 3) + 1#update the value of p multiplying by three and add one
    
    print(p)#print p each case it pass through the conditional 
