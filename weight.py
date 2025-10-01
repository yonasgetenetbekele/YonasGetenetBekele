#Python weight convertor 
weight = float(input('Please enter your weight: '))
unit = input ('Kilogram or Pounds? (K or L)')
if unit == "K":
    weight = round(weight *2.205)
    unit =="Lbs."
elif unit == "L":
    weight = round(weight/2.205)
    unit == "Kgs."
else:
    print(f'{unit} was not valid. Please enter either L or K to continue.')
print(f'Your weight is {weight} {unit}.')
