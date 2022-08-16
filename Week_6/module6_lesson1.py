# Create a list of integers between 5.5 and 20.5.

result = []
num = 5.5
while num < 21.5:
    result.append(num)
    num= num + 0.5
print(result)


#count the even and odd numbers in the list 
odd_num = list(filter(lambda x: (x%2 != 0), result))
odd_num = len(odd_num)
print(odd_num)

even_num = list(filter(lambda x: (x%2 == 0), result))
even_num = len(even_num)
print(even_num)


# square and cube every number in the list.
numbers_square= list(map(lambda x: (x**2), result))
print(numbers_square)


numbers_cube= list(map(lambda x: (x**3), result))
print(numbers_cube)






