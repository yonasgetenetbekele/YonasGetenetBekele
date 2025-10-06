#this is the dictionaries exercise in Python 

capitals = {"USA": "Washington D.C",
            "India": "New Delhi", 
            "China": "Beijing",
            "Russia": "Moscow"
            }
print (capitals.get ("USA"))
print (capitals.get("China"))
print (capitals.get("Russia"))

print (capitals.get("Japan"))

if capitals.get ("Russia"):
    print ("That capital exists.")
else:
    print ("This capital dosen't exist")

capitals.update ({"Germany": "Berlin"})
capitals.update ({"USA": "Detriot"})
capitals.pop ("China")
#capitals.popitem ()
#capitals.clear ()

values = capitals.values ()
for value in capitals.values ():
    print (value)
print (capitals)

items = capitals.items ()
print (items)
for key, value in capitals.items ():
    print (f"{key}: {value}")







