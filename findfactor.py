number = input("Enter a number (type quit to exit): ")

while True:
    if number == "quit":
        break

    number = int(number)
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
    number = input("Enter a number (type quit to exit): ")