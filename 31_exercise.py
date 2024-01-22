'''
when you give 
phone: 1234
output should be one two three four
'''
phone ={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
command = input("Phone : ")
for i in command:
    print(f'{phone[i]} ',end="")
