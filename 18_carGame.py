command = ""
started = False

while True:
    command=input('> ').lower()
    if(command=='start'):
        if started:
            print("Car Already Started")
        else:
            started = True
            print("Car Started....Ready to go!")
    elif(command=='stop'):
        if not started:
            print('Car Already Stopped')
        else:
         started = False
         print("Car is stopped")
    elif(command=='help'):
        print("""
start - To start the car
stop  - To stop the car
quit  - To exit
        """
        )
    elif command == 'quit':
        break
    else:
        print("I don't understand that")


'''
command = ""
start_car = False
stop_car =False
while True:
    command = input('>').lower()
    if command=='help':
        print("""
start - to start the car
stop - to stop the car'
quit - to exit
        """)
    elif command == 'start':
        if start_car==False :
         print("Car Started...Ready to go!")
         start_car=True
         stop_car=False
        else:
            print("Car Already started..")
    elif command == 'stop':
        if stop_car==False:
         print("Car Stopped.")
         stop_car=True
         start_car=False
        else:
           print("Car Already stopped")
    elif command == 'quit':
        break
    else:
        print("I don't understand that")
'''

'''
command =""
while True:
    command = input('>').lower()
    if command == 'help':
       print('start - to start the car')
       print('stop - to stop the car')
       print('quit - to exit')  
    elif command== 'start':
        print("Car Started...Ready to go!")
    elif command == 'stop':
         print("Car Stopped.")
    elif command == 'quit':
        break
    else:
        print("I don't understand that")
'''



     





  

