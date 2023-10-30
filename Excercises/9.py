x = input("Enter an x value (type quit to exit): ")

while True:
    if x == "quit":
        break
    
    x = int(x)
    if x < -2:
        print("y > 1")

    elif x <= 0:
        print("2 <= y < 3")

    elif x <= 3:
        print("0 <= y < 3")

    else:
        print("y = 4")
    
    x = input("Enter an x value (type quit to exit): ")