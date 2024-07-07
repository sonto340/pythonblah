def square(number):
    return number * number

# bad code below yuck
# result = square(3)
# print(result)
# instead do 
print(square(3))
# only because we are simply using the functions once.
# in a reusable funciton defining a variable is a better option

def mult(n1, n2):
    return n1 * n2 
x = 3 
y = 5

solution = mult(x, y)

hit_chance = solution / 3

print(int(hit_chance))