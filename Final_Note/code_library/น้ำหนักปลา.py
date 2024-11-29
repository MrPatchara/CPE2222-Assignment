fish = []

while True:
  weight = int(input())
  if weight == 0:
    break
  fish.append(weight)

sort = str(input())
if sort.lower() == "max":
  fish.sort(reverse=True)
else:
  fish.sort()

print(' '.join(map(str, fish)))