operator = input("Enter an operator (+ - / *)")
num1 = float(input('Enter the first number: '))
num2 = float(input ("Enter the second number: "))

#print (num1+num2)

if operator == "+":
    result = round(num1+num2)
    print(result)
elif operator == "-":
    result = round(num1-num2 )
    print(result)
elif operator == "*":
    result = round(num1*num2)
    print(result)
elif operator == "/":
    result = round(num1/num2)
    print (result)
else: 
    print('Please pick your operator to continue.')

#This is my Python calculator which can do the basic operators.
#I have also learnt concationation of string values unless we didn't declare the data type either float or integer.
