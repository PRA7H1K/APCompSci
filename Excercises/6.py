power_of_two = 1
exponent = 1
while power_of_two < 10000:
    print(f"2^ {str(exponent)} = {str(power_of_two)}")
    exponent = exponent + 1
    power_of_two = 2**exponent