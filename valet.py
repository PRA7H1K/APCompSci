temperature = int(input("What is the temperature?  "))

# Top
if temperature >= 75:
    print("You should wear a t-shirt")
elif temperature >= 50:
    print("You should wear long sleeve")
elif temperature >= 35:
    print("You should wear hoodie and t-shirt")
else:
    print("You should wear a coat")

#  Bottom
if temperature >= 40:
    print("You should wear shorts")
else:
    print("You should wear pants")

# Shoes
if temperature >= 65:
    print("You should wear sandals")
elif temperature >= 40:
    print("You should wear shoes")
else:
    print("You should wear boots")