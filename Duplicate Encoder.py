# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

# problem with KATA
''''
def duplicate_encode(word):
    #your code here
    nwrd=''
    upc = [int(+1) for y in word if y.isupper()==True]
    sw = [x for x in word.lower()]
    nwrd = ''.join(['(' if sw.count(n)>1 and n.islower()==True else ')' for n in sw])
    if sum(upc) >= 1:
        return ''.join(nwrd+','+'should ignore case')
    else:
        return nwrd
'''
'''
    for i in sw:
        if sw.count(i) > 1:
           nwrd = nwrd+'('
        else:
            nwrd = nwrd+')'

    return mwrd '''

#model answer
'''
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
'''

# adjusted from discussion.  # main point ignore Uppercase make everything lowercase.
def duplicate_encode(word):
    result = ""
    for i in word.lower():
        if word.lower().count(i) > 1 :
            result += ")"
        else:
            result += "("
            
    return result

if __name__=='__main__':
    s=input()
    print(duplicate_encode(s))