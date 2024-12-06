# โปรแกรมที่รับค่าจำนวนเต็ม 2 จำนวน และตรวจสอบว่าจำนวนใดมากกว่ากัน หรือเท่ากัน
myInput_1 = int(input())
myInput_2 = int(input())

if myInput_1 > myInput_2:
  print("A")
elif myInput_1 < myInput_2:
  print("B")
else:
  print("AB")