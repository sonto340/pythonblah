print('''An ancient looking car stands before you.
      You approach, seeing nobody nearby to whom it may belong.
      You slowly open the driver's side door, and get into the seat.''')
quit = "no"
car = "off"

while quit == "no":
    while car == "off":
        command = input("The car is off: ")
        if command.upper() == "QUIT":
            quit = "yes"
            break
        if command.upper() == "HELP":
            print('''Start - Start the car
                 Stop - Stop the car
                 Help - View this menu
                 Quit - Quit the game''')
        if command.upper() == "START":
            car = "on"
            print("The car roars to life with some effort. She sure is an antique...")
        if command.upper() == "STOP":
            print("Are you feeling okay? The car is already off...")
    while car == "on":
        command = input("The car rumbles away beneath you: ")
        if command.upper() == "QUIT":
            quit = "yes"
            break
        if command.upper() == "HELP":
            print('''Start - Start the car
                 Stop - Stop the car
                 Help - View this menu
                 Quit - Quit the game''')
        if command.upper() == "START":
            print("The car is already on. Surely you can feel that...? ")
            break
        if command.upper() == "STOP":
            car = "off"
            print("The car lurches to a sudden stop. Will it even start again?")
            break
while quit == "yes":
    print("Thanks for playing!")
    input()
    break
    