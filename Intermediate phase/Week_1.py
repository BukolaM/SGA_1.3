## '''Create a function, that repeats the first 2 letters of a word which will be followed by 3 dots and a space after. 
#The string should be ended with a question mark. Look below for examples'''

# Examples
# stutter("victor") ➞ vi... vi... victor?"

# stutter("amazing") ➞ "am... am... amazing?"

# stutter("good") ➞ "go... go... good?"'''






# def letter_repeat(x):
#     y = x[ :2] + '...' + ' ' + x[ :2] + '...' + ' ' +  x + '?'
#     return y

# letter = letter_repeat('victor')
# print(letter)

# letter = letter_repeat('amazing')
# print(letter)

# letter = letter_repeat('good')
# print(letter)




# # Sample String : 'abc', 'xyz'
# a = 'abc', 'xyz'
# k = a[0].replace('ab','xy')
# l = a[1].replace('xy','ab')

# j = k, l
# print(j)


# #Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def add_length(x):
    if len(x) >= 3:
        if x[-3:] == 'ing':
            x = x + "ly"
        else:
            x = x + "ing"
    return x

print(add_length('tosining'))




# Write a Python function that takes a list of words and return the longest word and the length of the longest one
def list_word(x):
    word = ''
    word_length = 0
    for a in x:
        b = len(a)
        if b > word_length:
            word_length = b 
            word = a
    return {
        'word': word,
        'length': word_length
    }
   

        
l = list_word(['bukola', 'go', 'come', 'eat', 'tosin'])
print(l['word'])


# Write a Python program to count repeated characters in a string. Go to the editor
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'

def repeat_count(word):
    tracker = {}
    for i in word:
        if i not in tracker.keys():
            tracker[i] = 1
        else:
            tracker[i] = tracker[i] + 1
    return tracker


print(repeat_count('bukolaajayi'))