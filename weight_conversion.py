weight = int(input("Weight:"))
rate = input("(L)bs or (K)gs: ")
if rate.upper() == "L":
    final = weight / 2.2
    print(f"You are {int(final)} kilos")
else:
    final = weight * 2.2
    print(f"You are {int(final)} pounds")