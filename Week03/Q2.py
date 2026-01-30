cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

#counting apples
apple_count = cart.count("apple")

#displaying how many apples in array
print("Number of apples: ", apple_count)

#finding milk position
milk_position = cart.index("milk")

#displaying milk position
print("Position of milk: ", milk_position)

#removing apple from the cart array
removed_item = cart.remove("apple")
print("Removed duplicate apple", cart)

removed_item = cart.pop()
print("Removed item using pop", cart)
print(f"Final cart: {cart}")