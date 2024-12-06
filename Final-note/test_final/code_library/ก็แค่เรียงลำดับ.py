# โปรแกรมรับค่าจำนวนเต็ม 5 ค่า และแสดงผลลัพธ์จากมากไปน้อย
num = 5
numb = []

for i in range(num):
  num = int(input())
  i += 1
  numb.append(num)
  
numb.sort(reverse=True)
for num in numb:
  print(num)