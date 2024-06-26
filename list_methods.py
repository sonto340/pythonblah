numbers = True
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy
numbers.append(10)
print(numbers)
print(numbers.copy)


check = 50 in numbers

machine_on = check

if machine_on:
    print("The machine is on.")
elif machine_on == False:
    print("The machine is off.")
