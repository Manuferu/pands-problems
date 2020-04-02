#########################################################################################################################
# Weekly task 7, Write a program that reads in a text file 
# and outputs the number of e's it contains. The program should take the filename from an argument on the command line
# Manuel Fernandez
#########################################################################################################################
#########################################################################################################################

import sys

# save in a variable the argument introduced by the user in the command line (it corresponds with the name of the file to open)
a=sys.argv[1:]
# Convert to string the text introduced by the user. It has to be transformed to string 'cause the variable a is a List format.
# to do that, we grab the firts and only value of the list and transform it to string format.
b=str(a[0])
#print(ord("E"))----> I have used ord build in expression to find out the character number or "E" (which is 69) and "e" (which is 101)
#print(ord("e"))----> I will use it below to find out those two characters
#Open a file using "with" statement. It is used "with" against "open", 'cause it takes care of closing the file 
# (source :https://realpython.com/read-write-files-python/#file-paths)


with open (b,'r') as f:
    #Iterate by each line of the file and set the counter to 0
    count=0
    for line in f:
        #iterate by each character in each line
        for char in line:
            # if character is "E" or character is "e", add it to the counter. If not continues with the next character
            if char==chr(101) or char==chr(69):                
                count+=1

# print the final count of E's and e's in the document 
print(count)
#The end 
                
          

       

