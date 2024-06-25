#while command.upper() == "HELP":
#    print('''start - to start the car
#        stop - to stop the car
#        quit - to exit  ''')
#    command == input()
#    break
#while command.upper() == "START:":
#    print("the car rumbles to life. She's an antique alright...")
#    command = input()
#if command.upper() == "HELP":
#    print('''start - to start the car
#        stop - to stop the car
#        quit - to exit  ''')
#    command = input()
#if command.upper() == "START":
#    print("The car rumbles to life. She's an antique alright...")
#    command = input()
#while command.upper() == "START":


#while state == "off":
#    command = input('Type to begin. Type "Help" for all options:')
#    if command.upper() == "HELP":
#        print('''start - to start the car
#        stop - to stop the car
#        quit - to exit  ''')
#    elif command.upper() == "START":
#        state = "on"
#        print("The engine roars to life. She's an antique alright...")
#    elif command.upper() == "STOP":
#        print("Come on, it's already off...")
#while state == "on":
#    command = input('Type to begin. Type "Help" for all options:')
#    if command.upper() == "HELP":
#        print('''start - to start the car
#        stop - to stop the car
#        quit - to exit  ''')
#    if command.upper() == "START":
#        print("Uhhm, it's still running already...")
#    if command.upper() == "STOP":
#        state == "off"
#        print("The car slowly clunks to a stop. I wonder if she'll start up again?")
#
state = "off"
quit = "no"
while quit == "no":
    while state == "off":
        command = input('Type to begin. Type "Help" for all options:')
        if command.upper() == "HELP":
            print('''
                start - to start the car
                stop - to stop the car
                quit - to exit  ''')
        if command.upper() == "START":
            state= "on"
            print("The car rumbles to life, she's an antique alright...")
        if command.upper() == "STOP":
            print("It's already off. Are you feeling alright?")
        if command.upper() == "QUIT:":
            quit = "yes"
           
    else:
        print('The car is chugging along harshly. ')
        command == input()
        if command.upper() == "HELP:":
            print('''
                start - to start the car
                stop - to stop the car
                quit - to exit  ''')
        if command.upper() == "START":
            print("It's uhh, already running. Surely you feel that?")
        if command.upper() == "STOP":
            print("The car comes to a hard and abrupt stop. Tough to say if it will start up again or not...")
            state = "off"
        if command.upper() == "QUIT":
            quit = "yes"
else:
    print("thanks for playing!")