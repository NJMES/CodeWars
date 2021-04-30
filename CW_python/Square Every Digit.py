# Square Every Digit 
# https://www.codewars.com/kata/546e2562b03326a88e000020/python'

'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9sq is 81 and 1sq is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    o = ''.join([str(int(x)**2) for x in str(num)])
    return int(o)

''' submission comment.
def square_digits(num):
    o = ''.join([str(int(x)**2) for x in str(num)]) 
    #run through num as string. convert x into int for square, then string back to be merge into a string.
    return int(o) #o is a string so output needs to be int.
'''

''' ideal ans:
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
'''