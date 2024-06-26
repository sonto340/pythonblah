numbers = [4, 6, 7, 7, 7, 7, 5, 5, 4, 4, 4]
removed = []
for number in numbers:
    if number is not removed:
        removed.append(number)
        numbers.remove(number)
print(removed)
print(numbers)
