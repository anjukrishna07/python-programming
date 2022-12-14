rows=int(input("enter number of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        square=i*j
        print(i*j,end=" ")
    print("")
//
output
enter number of rows:5
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
