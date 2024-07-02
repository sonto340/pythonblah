brent = input("brent's revenue:")
joseph = input("joseph's revenue:")
fernando = input("fernando's revenue:")


numbers = [brent, joseph, fernando]
max = numbers[0]
for number in numbers:
  if number > max:
    max = number
if number == brent:
  print("brent")
elif number == joseph:
  print("joseph")
elif number == fernando:
  print("fernando")
