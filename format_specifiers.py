#This is the format specifiers exercise 
price1 = 300000.14159
price2 = -98700.65
price3 = 1200.34

#decimal precision

print (f'Price 1 is ${price1: .1f}')
print (f'Price 2 is ${price2: .6f}')
print (f'Price 3 is ${price3: .3f}')

#Spaces

print (f'Price 1 is ${price1:10}')
print (f'Price 2 is ${price2:10}')
print (f'Price 3 is ${price3:10}')

#The zero paded justifer 

print (f'Price 1 is ${price1:010}')
print (f'Price 2 is ${price2:010}')
print (f'Price 3 is ${price3:010}')

#The left justifer 

print (f'Price 1 is ${price1:<10}')
print (f'Price 2 is ${price2:<10}')
print (f'Price 3 is ${price3:<10}')

#The right justifier 

print (f'Price 1 is ${price1:>10}')
print (f'Price 2 is ${price2:>10}')
print (f'Price 3 is ${price3:>10}')

#The central justifier

print (f'Price 1 is ${price1:^10}')
print (f'Price 2 is ${price2:^10}')
print (f'Price 3 is ${price3:^10}')

#The positive justifier 

print (f'Price 1 is ${price1:+}')
print (f'Price 2 is ${price2:+}')
print (f'Price 3 is ${price3:+}')

#The thousand separator

print (f'Price 1 is ${price1:,}')
print (f'Price 2 is ${price2:,}')
print (f'Price 3 is ${price3:,}')

#Combinations of formats and we can concatinate them as we want 

print (f'Price 1 is ${price1:+,.2f}')
print (f'Price 2 is ${price2:+,.2f}')
print (f'Price 3 is ${price3:+,.2f}')

