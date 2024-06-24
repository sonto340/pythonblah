name = input("Enter Name: ")

if len(name) <= 3:
    print("Error: Name must be at least 3 characters long")
elif len(name) >= 50:
    print("Error: Name must be less than 50 characters long")
else:
    print(f("Hello, {name}!"))
