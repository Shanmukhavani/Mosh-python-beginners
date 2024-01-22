#append() - used to add elements at the end of the list

list = [10,56,23,45,23]
list.append(50)
print(list) #[10, 56, 23, 45, 23, 50]

#insert() - used to insert elements at particular index
list.insert(0,40)
print(list) #[40, 10, 56, 23, 45, 23, 50]

#remove() - used to remove element
list.remove(10)
print(list) #[40, 56, 23, 45, 23, 50]

#clear()-used to remove all the elements in the list
list.clear()
print(list)  #[]

#pop() removes last item in the list.
list = [10,56,23,45,23]
list.pop()
print(list) #[10, 56, 23, 45]

#index() -used to check the existence of the element in the  list .
print(list.index(10)) #0 -returns the index of first occurance of a element
#print(list.index(100)) #ValueError: 100 is not in list

#in- it is also used to find the existence  of an element in the list.
print(50 in list) #False
print( 10 in list) #True

#count() - used to find the count of occurances of a number
print(list.count(10)) #1
print(list.count(90)) #0

#sort() - used to sort the elements in the list 
list.sort()
print(list)#[10, 23, 45, 56]

#reverse() -reverse the order of elements in the list
list.reverse()
print(list) #[56, 45, 23, 10]
list = [10,56,23,45,23]
list.reverse()
print(list) #[23, 45, 23, 56, 10]

#copy() -with this method you can get the copy of list
copy_list = list.copy()
print(f'copy_list ={copy_list}') #copy_list =[23, 45, 23, 56, 10]
copy_list[0]=100
print(copy_list) #[100, 45, 23, 56, 10]