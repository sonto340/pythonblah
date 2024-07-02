answer = 7
guesses = 0
guess_limit = 3
while guesses < guess_limit:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses += 1
    if guess == answer:
        print("Correct!~~")
        break
else:
    print("You Lose!!")
