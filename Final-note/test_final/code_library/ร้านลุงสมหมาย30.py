# โปรแกรมรับข้อมูลลูกค้า และแสดงข้อมูลลูกค้าทั้งหมด
cus = int(input())

customer = []

for i in range(cus):
  name = str(input())
  year = int(input())
  birth_year = 2017-year
  gender = input()
  customer.append((name, birth_year))
  i += 1

print("--Customers Information--")
for cust in customer:
  name, birth_year = cust
  print(f"{name} (age : {birth_year})")

#3 // บรรทัดแรกสุดบอกจำนวนลูกค้า
#K P //ลูกค้าคนที่ 1
#1990
#Male
#A A //ลูกค้าคนที่ 2
#2010
#Male
#Sommai KraiMakMak //ลูกค้าคนที่ 3
#1950
#Male
