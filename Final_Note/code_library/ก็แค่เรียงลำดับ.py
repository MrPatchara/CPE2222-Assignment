num = 5
numb = []

for i in range(num):
  num = int(input())
  i += 1
  numb.append(num)
  
numb.sort(reverse=True)
for num in numb:
  print(num)