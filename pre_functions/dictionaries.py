# curly brackets define a dictionary
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# square brackets pull value from a dictionary as shown
#   customer["name"] would show "John Smith"
# dictionaries can be modified or added to after the fact as shown
customer["name"] = "James West"
print(customer["name"])
# .get will look for the value and output None 
#   instead of an error
#   print(customer.get("birthdate"))
#   the above would output "None"

print(customer.get("birthyear"))