## creating a function with a list of numbers and the square of numbers 
# def squared(x):
#     dicti ={}
#     for y in x:
#         key = y
#         value = y**2
#         dicti[key] = value
#     return dicti

# a = squared([1,2,3,4,])
# print(a)

##Define a function that returns the maximum of any three numbers a user inputs. Assign the result to a variable “max_num”
# def maxi(y):
#    return max(y)
    
# b = maxi(range(10))
# print(b)


#Write a python program to generate and print a dictionary containing keys ranging from 5 to 15 (with both numbers included) and the values are the squares of the keys
# def ranging(y):     
#     for x in y:
#         key = {}
#         keys = x
#         values = x**2
#         key[keys] = values


#     return key

# a = ranging(range(5,16))
# print(a)


#1. '''Create a function, that repeats the first 2 letters of a word which will be followed by 3 dots and a space after. The string should be ended with a question mark'''. 
# def wording(result):
#     res = result[:2] + '...' + ' ' +  result[:2] + '...' + ' ?'
#     print(res)

# wording('everything')


# -------------------------------------------------------------------------------------

#2. Perform a for loop that searches through a string and prints only distinct vowel letters.
# def vowels_check(item):
#     vowels = ['a','e', 'i', 'o', 'u']
#     emp = []
#     for x in item:
#         if x in vowels and x not in emp: 
#             emp.append(x)

#     print(emp)


# vowels_check('honourable'
# --------------------------------------------------------------
# Sample_data = (3, 5, 7, 23)
# # all_list = Sample_data.split(',')
# all_list = list(Sample_data)
# print(all_list)


# ----------------------------------------------------------------
# 8. Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]
# a = color_list[0] + " "+ color_list[-1]
# print(a)



# # ------------------------------------------------------------------------
# Sample_String = 'google.com'
# empt = {}
# items = []
# for x in Sample_String:
#     if x not in items:
#         index = 0
#         items.append(x)
# # print (items)


# for a in items:
#         # key = a
#         # value = 0
#         empt[a] = 0
# # print(empt)


# for b in Sample_String:
#     #  key = b
#     #  value = empt[b] + 1 
#      empt[b] = empt[b] + 1 
# print(empt)

# ------------------------------------------------------
# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Go to the editor
# Sample String : 'w3resource'
# def string_length(item):
#     if len(item) < 2:
#         return ""
#     else: 
#         item = item[:2] + item[-2:]
#     return item


# y = string_length('w3resource')
# print(y)


# ------------------------------------------------------------
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# def add(item):
#     if item[-3:] == 'ing':
#         item = item + 'ly'
#         return item

#     if len(item) < 3:
#         item == item
#         return item

# y = add('abcing')
# print(y)


# -----------------------------------------------------------------------
# Write a Python function that takes a list of words and return the longest word and the length of the longest one
# def longest(items):
#     longest_item = ''
#     len_of_longest = 0
#     result = {}
#     for item in items:
#         if len(item) > len_of_longest:
#             longest_item = item
#             len_of_longest = len(item)
#     result['word'] =  longest_item
#     result['length'] = len_of_longest
#     return result


# y = longest(['exercises', 'sleep', 'gorilla', 'crocs'])
# print(y)

# ------------------------------------------------------
#  Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 
# def to_upper(items):
#     first_four = items[:4]
#     count_upper_case = 0
#     for a in first_four:
#         if a.isupper() is True:
#             count_upper_case = count_upper_case + 1
#     print(count_upper_case)
#     if count_upper_case >= 2:
#         return items.upper()
#     else:
#         return items
    
   
# y = to_upper('MAGNifY')
# print(y)


str1='Python Exercises\n'
print(str1.strip())
