
# Generate an array of numbers between 1 and 100 with both numbers included and find the LCM of the even numbers.&nbsp;
import numpy as np
array_1 = np.arange(1,101)
even_numbers = []
for arrays in array_1:
    if arrays % 2 == 0:
        even_numbers.append(arrays)
print(even_numbers)


#1.  to get the lcm using numpy 
arr = np.array(even_numbers)
result = np.lcm.reduce(arr)
print(result)
#'''the challenge with this is that when it got to number 84 and above the result start shifting 
# from positive to negative and was found that numpy.lcm() function can't handle large numbers'''



#2. however, if we use python function, and also import the math library, the lcm of the even numbers 
#can be gotten by declaring the even numbers as seen below.
import math
def LCMofArray(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])
    return lcm
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 
                40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68,70, 72, 74, 76,
                78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
lcm_of_even_numbers = LCMofArray(even_numbers)
print(lcm_of_even_numbers)




