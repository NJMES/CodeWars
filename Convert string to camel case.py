# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
'''

def to_camel_case(text):
#your code here
    ntext=''
    u=0            #on/off switch to know if any case needs to be converted.
    for i in text:                 #reading text char for char.
        if i == '-' or i =='_':    # if - or _ 
            ntext +=''               #add nothing. to new text.
            u+=1                     #switch on to turn next char upper.
        elif u==1:                    # if u switch is on.
            ntext += i.upper()        # make i upper. and write into new text.
            u=0                       # remember to switch off.
        else:
            ntext += i                # add i into new text.
    return ntext                      # return new text.

if __name__=='__main__':
    s=input()
    print(to_camel_case(s))

'''model ans
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
'''