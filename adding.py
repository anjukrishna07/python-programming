def addIngOrLy(str):
    if(str[-3:]=="ing"):
       str=str+"ly"
    else:
        str = str+"ing"
    return str
word=input("enter a word to modify:")
modifiedstring = addIngOrLy(word)
print("modifiedstring = ",modifiedstring)