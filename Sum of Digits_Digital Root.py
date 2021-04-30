# Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00/python

'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''

def digital_root(n):
    o=int(n)
    while len(str(o))>1:
        n = sum([int(x) for x in str(o)])
        o=n
        continue
    
    return o

''' my notation.
def digital_root(n):
    o=int(n)                                 # o = initial_n / subsiquent n values.
    while len(str(o))>1:                     #loop till single digits.
        n = sum([int(x) for x in str(o)])    #n= sum the all int(x) from running through string 'o' 
        o=n                                  # o takes one new number from n.
        continue                             #go back into loop to check 'digit' lenght.
    
    return o                                 #return the final value after breaking the loop.
'''
''' ideal ans:
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))    #digital_root() reference in here will create a loop
'''