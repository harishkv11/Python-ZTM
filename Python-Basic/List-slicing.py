#List Slicing --> Just like strings list can also be sliced using [x:y:z]

names = ['harish','rahul','prashant','pratyush','yash','harsh']

print(names) #Prints the whole list
print(names[0:2]) #Prints the names from 0 to 2(excluded)
print(names[::2]) #Prints every second name

#Lists are immutable --> data can be changed
names[2] = 'tanishq'
print(names)

#When we do list slicing, we create a new list
