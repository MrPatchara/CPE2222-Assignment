# โปรแกรมสร้างรูปแบบของบันไดด้วยเครื่องหมาย * โดยรับค่าจำนวนชั้นของบันได
ladder = int(input())
i = 1

while i-1 < ladder:
  print("*" * i)
  i += 1