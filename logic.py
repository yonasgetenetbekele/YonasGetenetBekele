#Logical operators
#Logical operators like and, or, and not are used especially in logical statements ie,. if statements.

temp = float(input('Enter the temprature in your house please. '))
if temp > 15 and temp <30: 
    print ("The temprature is good, no need of turning the ac on.")
else:
    print("Please turn on the AC!")
#In the and logical operator two of the conditions should be met.

#The or logical operator

weather =float(input("What is the weather in Ethiopia?"))
if weather <=0 or weather >=30:
    print ("The temprature is bad.")
else:
    print("The temprature is good.")

#Not logical operator 

temprature = 20
sunny = True
if not sunny:
    print('It is cloudy outside!')
else: 
    print ('It is sunny outside')