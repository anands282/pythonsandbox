addresses = ["123 Elm Street", "531 Oak Street", "678 Maple Street"]
street = "Elm Street"

# The top 2 methods to check if street in any of the items in the addresses list
# 1- Using the find method
for address in addresses:
    if address.find(street) >= 0:
        print(address)

# 2- Using the "in" keyword
for address in addresses:
    if street in address:
        print(address)