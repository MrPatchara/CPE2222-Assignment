amount = int(input())
piece = 0

for i in range(amount):
  price = int(input())
  piece += price

print(f"{piece} THB")
