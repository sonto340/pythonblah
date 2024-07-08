age_entered = False
while age_entered == False:

    try:
        age = int(input("Enter your age: "))
        income = 20000
        risk = income / age
        print(risk)
        age_entered = True
        break
    except ZeroDivisionError:
        print("Your age cannot be zero. Both in terms of the laws of physics and the purposes of this program.")
    except ValueError:
        print("That isn't a number...")
print("Code completed succesfully")
