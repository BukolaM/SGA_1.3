#1. '''Create a function, that repeats the first 2 letters of a word which will be followed by 3 dots and a space after. The string should be ended with a question mark'''. 
def word_repetition(item):
        word = item[ :2] + '...' + ' ' + item[ :2] + '...' + ' ' + item + '?'
        return word


result = word_repetition('victor')
print(result)

result = word_repetition('amazing')
print(result)

result = word_repetition('good')
print(result)



#2. Perform a for loop that searches through a string and prints only distinct vowel letters.
def vowels_search(item):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_list = []
    for i in item:
        if i in vowels and i not in vowels_list:
            vowels_list.append(i)
    return vowels_list

result = vowels_search('victor')
print(result)

result = vowels_search('amazing”')
print(result)

result = vowels_search('good')
print(result)



#3. Perform a while loop that requests for a name, if that name is entered, it will be printed else, if user types “end” (this command should be case insensitive), the while loop is terminated
item = True

while item == True:
    print('What is your name:' )
    name = input()

    if name.lower() == 'end':
        item = False
    else:
        print(name)
        


