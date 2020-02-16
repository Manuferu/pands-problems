#Task week 5, outputs if today is weekday or weekend.

import datetime
#Weekday of today
now =datetime.datetime.now().weekday()

L=[]
#iterate from 0 to 6
for i in range(0,7):
   #Create a Lit with 7 entries where the first 5 are considered weekday and th last 2 weekends.
    if i <5:
        L.append("Yes, unfortunately today is a weekday.")
    else:
        L.append("It is the weekend, yay!")
#Print the entry in the list that corresponds with the number of the variable now above created
print (L[now])

