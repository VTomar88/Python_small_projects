# This is a simple car game focuses on loop control and if statements

started = False
while True:
    user = input('> ').lower()
    # display help
    if user == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    # start the car
    elif user == 'start':
        # Check is car is not started
        if started:
            print('Car already started') # Keep the running if its running
        else:
            started = True # Make sure stop command is false while running
            print('Car started...Ready to go!')                      
    # stop the car
    elif user == 'stop':
        # Check if the car is stopped
        if not started:
            print('Car is already stopped')
        else:
            started = False # Make sure start command is false, if car is stopped
            print('Car stopped.') 
    # quit the game
    elif user == 'quit':
        break
    # different user response
    else:
        print("I don't understand that...")