number = int(input())
exponent = int(input())
result = 1

if exponent == 0:
    result = 1
else:
    while exponent > 0:
        result *= number
        exponent -= 1

print(f"{result}")
