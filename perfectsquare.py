import math
def isperfectsquare(x):
         if(x >= 0):
                 root = int(math.sqrt(x))
                 return((root*root)==x)
         return False
excludeList=[1,3,5,7,9]
evenlist=[2,4,6,8,0]
def allEven(num):
    while(num>0):
        if(num%10 in excludeList):
            return False
        else:
            num = num//10
    return True
def numbercombinations(x,y):
    for i in range(x,y+1):
        if(i//1000) not in excludeList:
            root=int(math.sqrt(i))
            if(isperfectsquare(i)):
                if allEven(i):
                    print("{},square of {}".format(i,int(math.sqrt(i))))
def takeInput():
    s_range = int(input("enter the starting range:"))
    f_range = int(input("enter the stopping range:"))
    if s_range>=1000 and f_range>=1000:
        numbercombinations(s_range,f_range)
    else:
        takeInput()
takeInput()

//
output
enter the starting range:2000
enter the stopping range:8000
4624,square of 68
6084,square of 78
6400,square of 80
