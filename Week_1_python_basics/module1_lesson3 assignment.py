
## creating a function with a list of numbers and the square of numbers 
def num_2(x):
    result={}
    index=0
    list_of_numbers = []
    for num in x:
        key=x[index]
        value= num*num
        result[key]=value
        index=index+1
    list_of_numbers.append(result)
    return list_of_numbers


y = num_2(range(5))
print(y)

