#1. Use else block to display a message “Done” after successful execution of for loop.
item = [0, 1, 2, 3, 4, 5, 6]
for i in item:
        print (i)       
else:
    print('Done')




#2. Write a program to display all prime numbers within a range.
def get_prime_numbers(item):
    prime = []
    for i in item:
        num = 0
        for r in range(1,i):
            if i % r == 0:
                num = num + 1
        if num == 1:
            prime.append(i)
    return prime

result = get_prime_numbers(range(21))
print (result)




#3. Use a loop to display elements from a given list present at odd index positions.
item = [1, 3, 4, 9, 5, 12, 7, 1, 5, 10, 40, 5, 2]
odd_index = []
num = 0
for i in item:
    if num % 2 != 0:
        odd_index.append(i) 
    num = num + 1

print(odd_index)





#4. Calculate the cube of all numbers from 1 to a given number
item = range(1, 11)
item_list = {}

for i in item:
    key = i
    value = i ** 3
    item_list[key] = value
print(item_list)


