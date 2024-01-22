'''
we use dictionaries if we want to store data in a key-pair value
'''
customer = {
    "name" : "JohnSmith",
    "age" : 30,
    "is_verified":True
}
print(customer["name"]) #JohnSmith
#print(customer["Name"])  #keyerror :'Name'
#print(customer["birthdate"]) #KeyError: 'birthdate'
'''
we have get() method , we can use it to get value of a key,the benifit of get() is even if u pass key which is 
not present in dictionary compiler wont yell to us .it just show none.

'''
print(customer.get("birthdate")) #None

#if that key is not present in the dictionary we can pass the value.
print(customer.get("birthdate" , "Dec 19")) #Dec 19
print(customer) #{'name': 'JohnSmith', 'age': 30, 'is_verified': True} , birthdate is not added yet,it just printed the value
# if you dont have that key u can pass value
#we can also modify values of keys in dictionary
customer["name"] ="Jack"
print(customer) #{'name': 'Jack', 'age': 30, 'is_verified': True}

#adding new key
customer["birthdate"] = ["Dec 19"]
print(customer) #{'name': 'Jack', 'age': 30, 'is_verified': True, 'birthdate': ['Dec 19']}

