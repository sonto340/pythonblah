# phone = input("Phone: ")
# numbers = {
#     "1" : "one",
#     "2" : "two",
#     "3" : "three",
#     "4" : "four",
#     "5" : "five",
#     "6" : "six",
#     "7" : "seven",
#     "8" : "eight",
#     "9" : "nine",
#     "0" : "zero"
# }
# output = ""
# for ch in phone:
#     output += numbers.get(ch, "*") + ""
# print(output)

message = input("Code your message: ")
scarmbler = {
    "a" : "q",
    "b" : "w",
    "c" : "e",
    "d" : "r",
    "e" : "t",
    "f" : "y",
    "g" : "u",
    "h" : "i",
    "i" : "o",
    "j" : "p",
    "k" : "a",
    "l" : "s",
    "m" : "d",
    "n" : "f",
    "o" : "g",
    "p" : "h",
    "q" : "j",
    "r" : "k",
    "s" : "l",
    "t" : "z",
    "u" : "x",
    "v" : "c",
    "w" : "v",
    "x" : "b",
    "y" : "n",
    "z" : "m",
    " " : "/"
}
coded = ""
for letter in message:
    coded +=scarmbler.get(letter, "*")

print('Your message has been sent to "coded.txt"')
with open("coded.txt", "w") as text_file:
    text_file.write(coded)
                