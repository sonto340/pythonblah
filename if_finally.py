import math
is_hot = False
is_cold = False
temp = input("What's the temperature outside?" )
if int(temp) > 85:
    is_hot = True
if int(temp) < 50:
    is_cold = True


if is_hot:
    print("It's a hot one!")
    print("Stay Hydrated!")
elif is_cold:
    print("It's a cold day!")
    print("Don't forget to bundle up!")
else:
    print("It's a lovely day!")
print("Enjoy your day!")