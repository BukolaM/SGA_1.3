# To create a dictionary function which takes the square of its input as the output
# in the range of 6
def the_square_of_number_range(x):
    result={}
    index=0

    for num in x:
       key = num
       value = num * num
       index = index + 1
       result[key] = value
    return result

y= the_square_of_number_range(range(5))
print (y)






