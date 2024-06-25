command = ""
started = False
while True:
    command = input("Input a command:").upper()
    if command == "HELP":
        print('''
Start - Start the car.
Stop - Stop the car.
Help - View this screen
Quit - Quit the game.''')
    if command == "START":
        if started:
            print("The car is rumbling away beneath you already.")
        else:
            started = True
            print("The car lurches to life beneath you. She sure is an antique...")
    elif command == "STOP":
        if not started:
            print("You'd have to turn it on first.")
        else:
            print("The car comes to a hard stop, and you find yourself wondering if it will ever start again...")
    elif command == "Quit":
        print("Thanks for playing!")
        break
    else:
        print("You'll have to enter a valid command. Type 'help' to see a list of commands.")
