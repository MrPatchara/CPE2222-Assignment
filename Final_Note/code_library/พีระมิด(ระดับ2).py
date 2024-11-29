myInput = int(input())
i = 1

while myInput > 0:
  print(f"{' ' * (myInput-1)}{'*' * i}")
  myInput -= 1
  i += 2
