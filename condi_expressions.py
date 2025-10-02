#This is conditional expressions in python
num =5 
num2= 6 
age = 19
weather = 26
print ('Positive' if num >0 else "Negative")
result = "Even " if num % 2 == 0 else 'Odd'
print (result)
max_num = "Num" if num>num2 else "Num 2"
print(max_num)
min_num = "Num" if num<num2 else "Num 2"
print(min_num)
status = "Adult" if age >=18 else "You are not eligible for the program."
weather = "Hot" if weather >25 else 'Cold'
print(status)
print(weather)
