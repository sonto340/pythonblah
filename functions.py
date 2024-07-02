# def sets a function that can be called multiple times
# parameters can be defined to more easily call them when referenceing the original function
def greet_user(first_name, last_name):
    print(f"Oh Hi {first_name} {last_name}")
# needs formated just like the print function and can you parameters in that formatting
    print("Welcome to the Thunder Dome")

greet_user("John", "Smith")
greet_user("Jason", "Griffith")
greet_user("Derek", "Geeter")