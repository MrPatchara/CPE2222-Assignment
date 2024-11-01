# Assignment III: การจัดการข้อมูลสินค้า
# รับข้อมูลสินค้า ราคา และจำนวนสินค้า
products = []
for i in range(3):
    print(f"Enter The {i+1}st Product Name:", end="") # รับชื่อสินค้า
    name = input()
    price = float(input(f"Enter Price of Product: "))
    quantity = int(input(f"Enter Quantity of Product: "))
    products.append((name, price, quantity))
    #products เป็นลิสต์ที่เก็บข้อมูลสินค้าทั้งหมด
    #ใช้ for loop จำนวน 3 ครั้งเพื่อรับข้อมูลของสินค้าทั้งสามตัว โดยในแต่ละรอบจะ:
    #แสดงข้อความให้ผู้ใช้ป้อนชื่อสินค้าตัวที่กำลังรับข้อมูล
    #เก็บข้อมูลของแต่ละสินค้าซึ่งประกอบด้วย name, price, และ quantity ไว้ใน products 

#ฟังก์ชัน display_inventory สำหรับแสดงรายการสินค้า
def display_inventory(items):
    print("\n" + "-" * 50)  # เส้นประด้านบน
    print(f"{'Inventory':^50}")  # แสดง "Inventory" อยู่ตรงกลาง
    print("-" * 50)  # เส้นประอีกครั้ง
    print(f"{'Item':>16}{'Price':>19}{'Quantity':>15}") 
    print("-" * 50)

    total_quantity = 0
    
    for item in items:
        name, price, quantity = item
        print(f"{name:<30}{price:<10}{quantity:>10}")
        total_quantity += quantity  
    
    print("-" * 50)
    total_line = f"Total Quantity = {total_quantity}"
    print(total_line.rjust(50))  # แสดงผลรวมของจำนวนสินค้าให้ชิดขวาสุด
    print("-" * 50)

# แสดงรายการสินค้าคงคลัง
display_inventory(products)
