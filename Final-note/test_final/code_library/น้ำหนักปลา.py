# โปรแกรมรับน้ำหนักของปลาจากผู้ใช้ จนกว่าผู้ใช้จะใส่ 0 แล้วแสดง
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