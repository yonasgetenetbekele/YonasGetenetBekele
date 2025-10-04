#For loops: will execute a block of code for a fixed amount of time 
for x in range(1,11, 3):
    print (x)
print ("Happy new year.")

#Interation over strings

credit_card = "2344-6543-4325"
for y in credit_card:
    print (y)

#The continue and break function

for x in range (1,21):
    if x == 13:
        break
    else: 
        print (x)

