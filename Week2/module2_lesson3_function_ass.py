##Write a python program to generate and print a dictionary containing keys ranging from 5 to 15 (with both numbers included) and the values are the squares of the keys

def numbers(number_range):
    numbers_key_values={}
    index=0

    for number in number_range:
        key=number_range[index]
        values=number * number
        index=index+1
        numbers_key_values[key]=values
        
    return numbers_key_values


result= numbers(range(5,16))
print(result)




