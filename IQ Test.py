#IQ Test

#https://www.codewars.com/kata/552c028c030765286c00007d/train/python

'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
Examples:

iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd
'''

def iq_test(numbers):
    #your code here
    ns=numbers.split()
    ct = [1 for x in ns if int(x)%2==0 ]
    if sum(ct) > 1:
        odd=[ns.index(y) for y in ns if int(y)%2!=0]
        return odd[0]+1
    else:
        even=[ns.index(z) for z in ns if int(z)%2==0]
        return even[0]+1

if __name__=='__main__':
    s=input()
    print(iq_test(s))

''' My notation.
def iq_test(numbers):
    #your code here
    ns=numbers.split()                                  # need to split the number up into list.
    ct = [1 for x in ns if int(x)%2==0 ]                # do a count if even is >1 
    if sum(ct) > 1:                                     # if even is >1 prioritise finding odd pos.
        odd=[ns.index(y) for y in ns if int(y)%2!=0]
        return odd[0]+1
    else:                                               # if even is not > 1
        even=[ns.index(z) for z in ns if int(z)%2==0]   # prioritise finding even position.
        return even[0]+1
'''

'''ideal ans
def iq_test(numbers):
    eo = [int(n)%2 for n in numbers.split()]
    return eo.index(1 if eo.count(0)>1 else 0)+1
'''