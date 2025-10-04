#This is the while loops exercise in Python
name = input ("Enter your name: ")
if name == "":
    print ("You did not enter your name. Please enter your name to continue.")
else:
    print (f'Hello {name}')

#The above is a simple if clause but what if we need to ask them to enter their name continually

#We will use the while loop

nom = str(input("Please enter your name: "))
while nom == "":
    print ("You did not enter your name")
    nom = str(input("Please enter your name: "))
print (f'Hello {nom}')

#While loop is a cycle that we use until we have achived whatever we want to execute, if we didn't the loop will continue untill we fulfill the requirments
#The infinite nature of while loop. unitl we introduce the user to escape from the loop. So create sth to help get off the loop.

age = int(input("Enter your age: "))

while age <0:
    print ("Age can't be negative")
    age = int(input('Please enter a valid age to continue: '))
print (f'Your are {age} years old.')

#Another example 

food = input("Enter the food you like the most or q to quit ")
while not food == "q":
    print (f'The food you like is {food}')
    food = input("Enter another food or q to quit")
print ('Bye')