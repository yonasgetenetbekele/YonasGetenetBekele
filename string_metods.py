#This is a string methods code
#1. The length function to find out the length of the characters
name = input("Please enter you name:")
result = len(name)
print (result)


#The find function helps to find the first occurence of a character. The index starts form 0,1,2,3...
find_fun= name.find("n")
print (find_fun)

#The last occurence of characters rfind.name....

reverse_find = name.rfind("s")

print (reverse_find)

#The capitalization function

capitalize_fun = name.capitalize ()
print (capitalize_fun)

#The uppercase function: .upper

uppercase = name.upper ()
print(uppercase)

#The lowercase function: .lower

lowercase = name.lower ()
print(lowercase)

#The numerical values identifier function: .isdigit

isdigit = name.isdigit ()
print (isdigit)

#The alphabet identifier: .isalpha

isalphabet = name.isalpha ()
print(isalphabet)

#The character counter method

phone_num = input("Please enter your phone number using dashes:")
charac_count = phone_num.count("-")

print(charac_count)

#The replace function 

replace_dashes = phone_num.replace ('-', " ")
print (replace_dashes)

#Everything combined

username =str(input('Please enter your user name: '))
if len(username) >12:
    print ("Your username can't be more than 12 characters.")
else: 
    print ("Recorded")