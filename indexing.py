#This is the string insdexing exercise in Python
#Indexing means acessing the elements of a sequence using []--the indexing operator [start: end: step]
credit_number = '1234-5678-7980'
print (credit_number[6])
print(credit_number[5:9])
print(credit_number [7:10])
print(credit_number[3:8])
print (credit_number [3:])
print(credit_number [:14])
#Indexing includes the starting index but not the ending index
#We can also use the negative indexing method to locate the elements of the list

print (credit_number [-1])
print (credit_number [-6])
print(credit_number [-14])

#There is also the step in the formula for indexing [start: end: step]
#The step function is acessing the elements after certain number of elements 

print (credit_number [::2])
print (credit_number [::3])

13-6878 and 146-8

last_digits = credit_number [-4:]
print (f'XXXX-XXXX-XXXX-{last_digits}')

#Conclusion: The indexing is performed using the indexing the square bracket
#And the form of indexing is [start: end: step]
#The step means that take the member of the elements after certain number of 
#steps starting from the first member of the list




