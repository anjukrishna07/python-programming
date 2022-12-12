def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1: ]
    return str1
a=input("enter a string:\n")
print(change_char(a))
