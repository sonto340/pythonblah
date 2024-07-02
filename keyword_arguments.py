def greet_user(first_name, last_name):
    print(f"Oh Hi {first_name} {last_name}")
    print("Welcome to the Thunder Dome")

# greet_user("John", "Smith")
# these are called positional arguments because their position matters
greet_user(last_name="Smith", first_name="John")
# these are keyword arguments. they are defined no matter the order
# usually best to use positional unless readibility of code is a better options
# pyhton must process positional arguments first

# calc_cost(total=50, shipping=5, discount=0.1)
#this is an example of keywords being better because otherwise it's just seemingly random numbers

