#This is the nested loop exercise
#Nested loop is a loop within another loop (outer, inner)
#Use indentation to separate the outer and inner loops 

rows = int(input ("Enter the number of rows: "))
columns = int (input ("Enter the number of columns: "))
symbol = input ("Enter a symbol to use")
for x in range (rows):
    for y in range (columns):
        print(symbol, end="")
    print ()

        
