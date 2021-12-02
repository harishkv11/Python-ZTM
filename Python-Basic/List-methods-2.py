basket = [1,2,3,4,5,6,7,8]

#index --> Return first index of a number ---> list.index(value,starting,ending)
print(basket.index(3,0,8))
print(basket.index(3)) #prints the same result

#in keyword --> returns true if element is present in the list
print(1 in basket) #True
print(20 in basket) #False

#count --> Return the total occurance of an element
print(basket.count(2))
