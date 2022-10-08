
from asyncio import constants


x = 'google.com'
all_list = []
for y in x:
    if y not in all_list:
        all_list.append(y)

dict = {}
for a in all_list:
    key = a
    value = 0
    dict[key] = value

for b in x:
    key = b
    dict[key] = dict[key] + 1



nums = (1,2)
# print(2 * nums)


def get_char(x):
    x = 'w3resource'
    if len(x) > 2:
        y = x[0:2] + x[-2:]
        return y
    else:
        return 'none'
    


# Write a Python program to count and display the vowels of a given text
a = 'w3resource'
vowels = ['a','e','i','o','u']
tee = []
constants
for all in a:
    if all not in vowels:
        tee.append(all)
    else:
        print()

