# Sum of Digits in Integer

# Enter Integer
integer = int(input("Enter desired integer between 0 to 1000: "))

# narrowing of values to between 0 to 1000
if 0 <= integer <= 1000:
    integer = integer
elif integer < 0:
    print("Your desired integer is too small. Please try again with a larger integer. ")
else:
    print("Your desired integer is too large. Please try again with a smaller integer. ")

# adding up the digits
if 0 <= integer < 10:
    digit1 = integer % 10
    print(digit1)
elif 10 <= integer < 100:
    digit1 = integer % 10
    integer = integer // 10
    digit2 = integer % 10
    total = digit1 + digit2
    print(total)
elif 100 <= integer < 1000:
    digit1 = integer % 10
    integer = integer // 10
    digit2 = integer % 10
    integer = integer // 10
    digit3 = integer % 10
    total = digit1 + digit2 + digit3
    print(total)
else:
    digit1 = integer % 10
    integer = integer // 10
    digit2 = integer % 10
    integer = integer // 10
    digit3 = integer % 10
    integer = integer // 10
    digit4 = integer % 10
    total = digit1 + digit2 + digit3 + digit4
    print(total)