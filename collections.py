#Collections in python List, set, and tuples
fruits = ['apple', "orange", "banana", "cocunut"]
print (dir(fruits))
print (fruits[0:4:1])
print(len(fruits))
for fruit in fruits:
    print (fruit)
print ("pineapple" in fruits)

fruits[1] = 'pineapple'
for fruit in fruits:
    print (fruit, "")

fruits.append ("pineapple")
fruits.remove ("apple")
fruits.insert (0, "pineapple")
fruits.sort ()
fruits.reverse ()
fruits.clear ()
print(fruits.count ("banana"))
print (fruits)

books = {"apple", "orange", "banana", "cocunut"}
print (len(books))
books.add ("Holmes")
books.clear
books.remove ("Holmes")
print (books)

#Tuples 

tuples = ("apples", "orange", "banana", "cocunut")
print (tuples)
print(len(tuples))
print (tuples.index ("apples"))

for book in books:
    print (book)


