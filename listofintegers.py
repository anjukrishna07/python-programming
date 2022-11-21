len=int(input("how many number do you want to store?"))
input_valuelist=[]
for num in range (0,len):
    input_value=int(input("enter a value"))
    if input_value>=100:
        input_valuelist.append("over")
    else:
        input_valuelist.append(input_value)
print(input_valuelist)
  
