#This is a two dimentional list in Python
groceries = [['apples', 'orange', 'banana', 'cocunut'], 
             ['celery', 'carrots', 'potatoes'], 
             ['chicken', 'fsih',  'turkey']]
for collection in groceries:
    for food in collection:
        print (food, end=" ")
    print ()

num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))   
for row in num_pad:
    for num in row:
        print (num, end =" ")
    print ()