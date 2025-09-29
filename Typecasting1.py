#This is my typecasting exercise
name = ("Yonas")
age = 17
average = 99.98
male = True \

#Now let us print the types of the data 

print (type(name))
print (type (age))
print (type(average))
print(type(male))

#Converting one data type into another 

age = float(age)
print (age)
print (type(age))

#now the data type of age is changed from integer to float.

average =int(average)
print (average)
print (type(average))

#Here I have changed a float to an integer 

male = str(male)
print (male)
print (type(male))

#I have changed the boolean Male into a string 

age = bool(age)
print (age)
print(type(age))

#Here I have converted a string into a boolean;
#and still the output is True because we have a value
#into the parenthessis. The only reason the boolean value will
#false is if the value of the number is zero. and also for string 
#The only reason for the boolean value to be false is either the
#value of the of the integer/float is zero or we have a null/empty
# Parenthesis.

#We use the casting function to know the type of the data and 
#Convert one data type into another. 

x=2
y=2.0
x=x/y

print(x)

#In implict type casting the programming language automatically
#converts from one type to another if needed. 






