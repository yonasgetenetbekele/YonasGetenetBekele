#Python Temprature Conversion Program 
unit = input("Is this temprature in Celcius or Fahrenheit (C/F)")
temp =float(input ("Enter the temprature: "))
if unit =='C':
    temp= round(temp*1.8+32, 2)
    print (f'Your temprature is {temp} F')
elif unit == "F":
    temp =round((temp-32)*0.55, 2)
    print (f'Your temprature is {temp} C')
else:
    print(f'{temp} is invalid, please input either C for Celcius or F for Farhenheight.')