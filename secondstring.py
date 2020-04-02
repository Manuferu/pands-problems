# Manuel Fernandez
# Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

# Sentence introducing by the user

s = input("Please enter a sentence:")

# start the counting from the end of the sentence stored in variable s
# to the start, grabing letter each 2 position reverse
print(s[len(s):0:-2])