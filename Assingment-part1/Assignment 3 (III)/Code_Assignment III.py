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
    #รับข้อมูล ชื่อสินค้า (name) โดยใช้ input()
    #รับข้อมูล ราคาสินค้า (price) และแปลงเป็นชนิด float
    #รับข้อมูล จำนวนสินค้า (quantity) และแปลงเป็นชนิด int
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
    #แสดงส่วนหัว: ฟังก์ชันนี้เริ่มต้นด้วยการแสดงชื่อ "Inventory" อยู่กลางบรรทัด โดยใช้ f-string พร้อมด้วยเส้นประที่เป็นการคั่นบรรทัดด้านบนและล่างเพื่อความสวยงาม
    #หัวตาราง: แสดงหัวข้อ "Item", "Price", และ "Quantity" พร้อมการจัดตำแหน่งให้เหมาะสม (เช่น >16 เพื่อจัดชิดขวาที่ตำแหน่งคอลัมน์ 16)
    #ตัวแปร total_quantity: ใช้เก็บผลรวมของจำนวนสินค้าทั้งหมด
    #แสดงรายละเอียดสินค้า: ใช้ for loop เพื่อดึงข้อมูลของสินค้าทีละรายการจาก items 
    #ซึ่งอยู่ในรูปแบบของ tuple และแสดงชื่อ (name), ราคา 
    # (price), และจำนวน (quantity) ของสินค้าแต่ละตัว โดยจัดเรียงตามตำแหน่งที่กำหนดใน f-string
    #name:<30 จัดชิดซ้ายในคอลัมน์ขนาด 30 ตัวอักษร
    #price:<10 จัดชิดซ้ายในคอลัมน์ขนาด 10 ตัวอักษร
    #quantity:>10 จัดชิดขวาในคอลัมน์ขนาด 10 ตัวอักษร
    #คำนวณผลรวมจำนวนสินค้า: เพิ่มค่าของ quantity แต่ละสินค้าเข้าไปใน total_quantity
    #แสดงผลรวม: แสดงข้อความผลรวมของจำนวนสินค้าโดยจัดให้อยู่ขวาสุดของบรรทัด (total_line.rjust(50)) และปิดท้ายด้วยเส้นประ

# แสดงรายการสินค้าคงคลัง
display_inventory(products)
