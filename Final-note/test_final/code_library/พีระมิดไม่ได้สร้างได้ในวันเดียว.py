# โปรแกรมสร้างรูปสามเหลี่ยมด้านเท่าที่มีด้านเป็นเลขคู่
myInput = int(input())
i = 5
j = 1

while myInput-1 >= 0:
  print(f"{' ' * int(myInput - 1) }{'*' * j}")
  i -= 1
  j += 2
  myInput -= 1
  