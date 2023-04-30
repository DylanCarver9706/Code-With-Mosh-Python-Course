print("Welcome to the car game!")
print("start - to start the car")
print("stop - to stop the car")
print("quit - to exit the game")
print("help - to show these commands again")
user_input = ""
started_status = False

while True:
    user_input = input("> ").lower()
    if user_input == "start" and started_status == True:
        print("The car is already started")
    elif user_input == "start":
        started_status = True
        print("The car has started!")
    elif user_input == "stop" and started_status == False:
        print("The car is already stopped")
    elif user_input == "stop":
        started_status = False
        print("The car is stopped")
    elif user_input == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit the game")
        print("help - to show these commands again")
    elif user_input == "quit":
        break
    else:
        print("Sorry I don't understand that")


