# for x in range(4):
#    for y in range(3):
#        print(f"({x}, {y})")
# numbers = [1, 1, 1, 6, 6]
# for x in numbers:
#    output = ""
#    for count in range(x):
#        output += "x"
#    print(output)

# numbers = [4, 5, 7, 7]
# for x in numbers:
#    for y in numbers:
#        print(f"Value:({x+1},{y})")


numbers = [5, 8, 27]

for x in numbers:
    while x < 20:
        print((x + 1) * 2)
        x += 1
