Input1 = int(input())
Input2 = int(input())
Input3 = int(input())

Max = Input1

if Input2 > Max:
  Max = Input2

elif Input3 > Max:
  Max = Input3

print(f"MAX : {Max}")