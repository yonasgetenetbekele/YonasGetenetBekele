#This is an if statement code 
age=int(input("What's your age?: "))
if age >=18:
    print("Your are eligible to apply for the program!")
elif age <0:
    print("You haven't born yet! Haaa!")
elif age >100:
    print("Sorry, You are too old to apply!")
else: 
    print("You are not eligible for this program!")

#The food example

response=input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food.")
else:
    print("No food for you.")

#The name example

name =str(input("Write your name to continue: "))
if name=='':
    print("Please write your name in the space provide to continue.")
else:
    print(f'Hello {name}!')

