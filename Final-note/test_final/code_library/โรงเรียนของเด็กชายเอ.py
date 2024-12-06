# โปรแกรมคำนวณเกรด
myInput = int(input())
Grade = 0

if myInput >= 90:
  Grade = "A"
  
elif myInput >= 85:
  Grade = "B+"

elif myInput >= 80:
  Grade = "B"

elif myInput >= 75:
  Grade = "C+"

elif myInput >= 70:
  Grade = "C"

elif myInput >= 65:
  Grade = "D+"

elif myInput >= 60:
  Grade = "D"

else:
  Grade = "F"

print(Grade)
