coded = input("Enter your coded message: ")
decoder = {
    "q" : "a",
    "w" : "b",
    "e" : "c",
    "r" : "d",
    "t" : "e",
    "y" : "f",
    "u" : "g",
    "i" : "h",
    "o" : "i",
    "p" : "j",
    "a" : "k",
    "s" : "l",
    "d" : "m",
    "f" : "n",
    "g" : "o",
    "h" : "p",
    "j" : "q",
    "k" : "r",
    "l" : "s",
    "z" : "t",
    "x" : "u",
    "c" : "v",
    "v" : "w",
    "b" : "x",
    "n" : "y",
    "m" : "z",
    "/" : " "
}
decoded = ""
for ch in coded:
    decoded += decoder.get(ch, "*")

print ('your message has been sent to "decoded.txt')
with open("decoded.txt", "w") as text_file:
    text_file.write(decoded)