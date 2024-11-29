n = int(input())
i = 1

if n == 0:
  print(i)

else:
  while True:
    i = n * i
    n -= 1

    if n <= 0:
      print(i)
      break