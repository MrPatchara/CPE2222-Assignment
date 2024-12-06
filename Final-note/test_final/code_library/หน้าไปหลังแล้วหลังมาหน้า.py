# โปรแกรมรับค่าจำนวนเต็ม n และรับค่าจำนวนเต็ม n ตัว แล้วแสดงผลลัพธ์จากหลังมาหน้า
num = int(input())
numa = []

for i in range(num):
  numb = int(input())
  i += 1
  numa.append(numb)

numa.reverse()
for numa in numa:
  print(numa)
  