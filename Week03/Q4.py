monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
#Appending grace to monday class
monday_class.add("Grace")
print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")
print(f"Attended both class: {monday_class & wednesday_class}") # & = shift + 7
print(f"Attended either class: {monday_class | wednesday_class}") # | =pipe, shift + \
print(f"Only Attended Monday Class: {monday_class - wednesday_class}")
print(f"Only attended one class (Not both): {monday_class ^ wednesday_class}"  ) # ^ = caret
all_classes = monday_class | wednesday_class
print("Is Monday subset of all students? ", monday_class <= all_classes) # True