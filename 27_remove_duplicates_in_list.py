list = [10,20,20,50,30,20,40,10,10]
unique_list=[]
for x in list:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)
#output :[10, 20, 50, 30, 40]
    