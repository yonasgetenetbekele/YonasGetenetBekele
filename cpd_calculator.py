#This is the compound interst calcualtor 

principal = 0
rate = 0
time = 0

while principal <=0:
    principal = float(input('Enter the principal:'))
    if principal <=0:
        print ("Principal can't be less than zero.")

while rate <=0:
    rate = float(input('Enter the interst rate:'))
    if rate <=0:
        print ("Rate can't be less than zero.")
        
while time <=0:
    time = int(input('Enter the time of the investment:'))
    if time <=0:
        print ("Time can't be less than zero.")
        
total = principal * pow((1+rate/100), time)     
print (f'Balance after {time} years of investment is ${total: .2f}.')
