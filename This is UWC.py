#This is UWC Changshu China Campus 
print ("This is UWC Changshu China Campus: The best UWC campus ever!")
print ("Yonas Getenet Bekele")
first_name = "Yonas"
last_name = "Bekele"
middle_name = "Getenet"
full_name = first_name + middle_name + last_name
print (full_name)
print (f'My full name is {first_name} {middle_name} {last_name}.')
age =16 

#Strings and f-strings 

food = "Doro Wat"
print (f'My name is {first_name} {middle_name} {last_name}, I am {age} years old and my favorite food is {food}.')
email ="yonasfake@gmail.com"
print (f'My email is {email} and shoot me at whatever time you want!')

#Integers are usually whole numbers that are unsed for counting purposes and they don't take a quotation marks as a string unless and otherwise they will be considered as strings. 

print (f'You are {age} years old.')

#f strings are used to format strings and they are usually used when we want to include or combine variables and strings together.
id_number = 2394943 
print (f'Your id number is {id_number} and use is always for identification and verification purposes.')
height = 1.75 
print ("What is your height in meters?")
print (f'My height is {height} meters.')
weight = 70
print (f'My weight is {weight} kilograms')\


#float are usually decimal numbers and they are used when we want to be more precise about a number. And also they will show precision in our numbers. 
#integers don't take string quoatation marks otherwise they will be considered as strings. 
gpa =3.883

print (f'My gpa is {gpa} and it needs improvement to be 4.0 and hopefully I will get it next semester.')
#let us continue with some more examples of strings and floats and then we will procceed to booleans, which have two values either true or false. 

#for booleans, use either True or False and, use capital letters for the first letter of the word.

if_student = False 

if if_student: 
    print ("You are a student.")
else: 
    print ("You are not a student or you are a recent graduate.")
    
if_male = True 

if if_male: 
    print (f'You are a male student and your name is {first_name} {middle_name} {last_name}.')
else: 
    print ("You are female student.")

if_tall = False 
if if_tall:
    print ("You are allowed to get into the campus to play baketball.")
else: 
    print ("Sorry you are not tall enough to play basketball in the campus. If you want to play an other sports, please do let us know and we will arrange it for you.")


#more if clauses to practice booleans.
if_uwc_student = True 
if if_uwc_student: 
    print (f'Congratulations {first_name} {last_name}, you are UWCer and continue making a difference in the world. Additionally, work to make eduaction a force to unite people, nations and cultures for peace and a sustainable future.')
else: 
    print ("You are not a UWCer, but you can always apply to be one and make a difference in your community and the world as well.")


if_uwc_changshu_student = True 
if if_uwc_changshu_student:
    print ("You are lucky and enjoy your time at UWC Changshu China Campus, the best UWC campus ever!")
else:
    print ("Unfortunately, you are not member of United World College of Changshu China Campus, but other UWC campuses are also great and use the resources that UWC has to offer.")

if_youtake_chemistry = False
if if_youtake_chemistry:
    print ("You are going to have a great time in IB chemistry and it has one of the long internal assessmets though.")
else: 
    print ("You are not interested in chemistry, but you can always take other sciences like computer science, physics and enviromental systems and societies, as UWC Changshu offers various courses to select from.")
    
