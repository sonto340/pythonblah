#for x in range(4):
#    for y in range(3):
#        print(f"({x}, {y})")
numbers = [1, 1, 1, 6, 6]
for x in numbers:
    output = ""
    for count in range(x):
        output += "x"
    print(output)