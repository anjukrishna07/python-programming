num=int(input("enter the value:"))
print("the fibonacci series is:")
def fibonacci(num):
    n1=0
    n2=1
    count=0
    print(n1)
    print(n2)
    while(count<num-2):
         num3=n1+n2
         print(num3)
         n1=num3
         count=count+1
fibonacci(num)