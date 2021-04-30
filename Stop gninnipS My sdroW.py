# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

'''model answer
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
'''
    
def spin_words(sentence):
    # Your code goes here
    sen = sentence.split()  #split input into list elem
    brk = []                #new list to store.
    for x in sen:           #index individual words in list.
        if len(x) >= 5:           #if word length >= 5 
            brk.append(x[::-1])    # reverse the word using x[::-1]
        elif len(x) < 5:            # if shorted then 5
            brk.append(x)            # add to new list as per input.
    return ' '.join(brk)            #return the list in a String.


if __name__=='__main__':
    s=input()
    print(spin_words(s))
    