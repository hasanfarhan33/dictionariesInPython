#       {Key:Value}
names = {1:"Farhan", 2:"Faizan",
         3:"Ege", 4:"Baris", 5:"Enver"}

print(names)
print("Keys: ", names.keys())
print("Values: ", names.values())
print("names[2]: ", names[2])
print("names[5]: ", names[5])
print()
print("__get()__")
print(names.get(4))
print(names.get(3))
names[7] = names.get(7, "Phony")
print(names)

print()
print("__items()__")
print(names.items())