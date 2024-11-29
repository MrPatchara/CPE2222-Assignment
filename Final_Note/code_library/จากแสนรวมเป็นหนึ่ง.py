num = int(input())

while num >= 10:
  num = sum(int(numa) for numa in str(num))

print(num)