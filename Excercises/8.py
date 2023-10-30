first = int(input("First Number: "))
second = int(input("Second Number: "))

while first % second != 0:
    print(f"{first} is NOT divisible by {second}")

    first = int(input("First Number: "))
    second = int(input("Second Number: "))

print(f"{first} is divisible by {second}")