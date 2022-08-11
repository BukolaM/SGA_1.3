# def number(x,y):
#     output=x**y
#     if output==0:
#         return 1
#     else:
#         return output

# my_result = number (2,4)
# print (my_result)


# k= number(5,2)
# print(k)


# l= number(16,10)
# print(l)



###------------------------------------------------------
# item=['cheescake','applepie','icecream']
# price=[2,3,4]
# menu={}
# index=0

# for items in item:
#  itemss= items[index]
#  prices= price[index]
#  index=index+1
#  menu[itemss]=prices
# print(menu)
##-----------------------------------------------------------



##bring out the square of a list to a dict
# the_dict={}
# itemssss=[]
# def item_a(x):
#     for ans in x:
#         ans = ans * ans
#         itemssss.append[ans]
#     return itemssss




# y=item_a([0,1,2,3,4,5])
# print(y)




# dicti={}
# item=[]

# itemssss=[2,4,6,8,9]
# for ans in itemssss:
#     ans = ans * ans
#     item.append(ans)  

# index=0

# for x in itemssss:
#     key_item= itemssss[index]
#     value_key=item[index]
#     index=index +1
#     dicti[key_item]=value_key
# print(dicti)


# x=['cheese','burger','cake','fruit']
# c=0
# for y in x:
#     print(y)
#     print(x[c])
#     c=c+1





## creating a function with a list of numbers and the square of numbers 

# def numbers (x):
#     square_of_numbers = []
#     for number in x:
#         number = number * number
#         square_of_numbers.append(number)
#     result={}
#     index=0

#     for b in x:
#         item_key=x[index]
#         item_value=square_of_numbers[index]
#         index=index+1
#         result[item_key]=item_value
#     return  result




def num_2(x):
    result={}
    index=0
    for num in x:
        key=x[index]
        value= num*num
        result[key]=value
        index=index+1
    return result



y= num_2(range(5))
print(y)