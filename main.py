""" Write a python program to build a Bitwise Swap Challenge using Python. They will practise swapping values without a third variable, using XOR swap, using
left shift to double numbers, detecting different signs with XOR, and dividing numbers without using the / operator."""

print("Swap without 3rd Variable")
a = 76
b = 14

print("Before Swap")
print(f"a: {a}")
print(f"b: {b}")
print()

a = a + b
b = a - b
a = a - b

print("After Swap")
print(f"a: {a}")
print(f"b: {b}")
print()

print("XOR Swap")
x = 46
y = 18

print("Before XOR Swap")
print(f"x: {x}")
print(f"y: {y}")
print()

x = x ^ y
y = x ^ y
x = x ^ y

print("After XOR Swap")
print(f"x: {x}")
print(f"y: {y}")
print()

print("Left Shift")
number = 6

print(f"Original: {number}")
print(f"number << 1: {number << 1}")
print(f"number << 2: {number << 2}")
print(f"number << 3: {number << 3}")
print(f"number << 4: { number << 4}")
print()

print("XOR for Sign Detection")
num1 = -12
num2 = 6

print(f"num1: {num1}")
print(f"num2: {num2}")

if (num1 < 0) ^ (num2 < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")
print()

print("Divide w/o /")
dividend = 25
divisor = 4

quotient = 0
remainder = dividend

while remainder >= divisor:
    remainder = remainder - divisor
    quotient = quotient + 1

print(f"Dividend: {dividend}")
print(f"Divisor:{divisor}")
print(f"Quotient: {quotient}")
print(f"Remainder:{remainder}")