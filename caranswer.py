command = ""
started = False
while True:
    command = input("> ").upper()
    if command == "START":
        if started:
            print("It's already on!")
        else:
            print("The car started.")
            started = True
    elif command == "STOP":
        if not started:
            print("the car is already off")
        else:
            print("The car stopped.")
            started = False
    elif command == "HELP":
        print(''' 
Start - Start the car
Stop - Stop the car
Quit- End the program''')
    elif command == "QUIT":
        print("Thanks for playing!")
        break
    else:
        print("Sorry try entering a valid command")


