# โปรแกรมค้นหารหัสสินค้า
n = int(input())

code_pkg = []

for i in range(n):
  code = input()
  code_pkg.append(code)
  i += 1

search_pkg = input()

found_pkg = [i+1 for i, pkg in enumerate(code_pkg) if pkg == search_pkg]

if found_pkg:
  print(f"Position: {','.join(map(str, found_pkg))}")
else:
  print("2")

#บรรทัดแรก n เป็นจำนวนของสินค้าทั้งหมด
#บรรทัด n ต่อไป เป็นรหัสสินค้าเป็นเลขจำนวนเต็ม
#บรรทัดสุดท้ายเป็นรหัสสินค้าที่ต้องการหา เป็นเลขจำนวนเต็ม