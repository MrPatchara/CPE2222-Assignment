# โปรแกรมที่รับค่าจำนวนเต็มจากผู้ใช้ และหาผลรวมของเลขทุกตัวในตัวเลขนั้น จนกว่าจะเหลือเลขตัวเดียว
num = int(input())

while num >= 10:
  num = sum(int(numa) for numa in str(num))

print(num)