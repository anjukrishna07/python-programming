firstnamelist=[]
len=int(input("how many names do you want to insert"))
for i in range(0,len):
    fname=input("enter the first name you want to add to list")
    firstnamelist.append(fname)
    count_a=0
for name in firstnamelist:
        count_a+=name.count("a")
print(count_a)
