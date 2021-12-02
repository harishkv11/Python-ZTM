basket = [1,2,3,4,5,6,7]

#len(basket) --> return size of list
print(len(basket))

#append --> Appends an object to the end, does not return anything
basket.append(10)
print(basket)

#insert --> Insert an object at index
#list.insert(index,value)

basket.insert(2,100)
print(basket)

#extend --> Adds on a new list to the end of the list
basket.extend([1,1,1])
print(basket)

#pop --> Removes the last element, it also returns a element
basket.pop()
print(basket)

basket.pop(2) #Removes the element at index 2
print(basket)

#remove --> Removes a particular value
basket.remove(1)
print(basket)

#clear --> Removes all the elements from the list
basket.clear()
print(basket)