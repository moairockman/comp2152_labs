contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(f"Alice's number: {contacts["Alice"]}")
#adding Diana's Number

contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")

# updating bob's number
contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob: {contacts}")
#deleting Charlie's number
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

#listing all the names
print(f"All names: {contacts.keys()}")

#listing all the numbers
print(f"All numbers: {contacts.values()}")

#listing the total number of contacts
print(f"Total Contacts {len(contacts)}")