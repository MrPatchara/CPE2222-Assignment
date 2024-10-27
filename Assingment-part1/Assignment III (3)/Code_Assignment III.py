# รับข้อมูลสินค้า ราคา และจำนวนสินค้า
products = []
for i in range(3):
    print(f"Enter The {i+1}st Product Name:", end="") # รับชื่อสินค้า
    name = input()
    price = float(input(f"Enter Price of Product: "))
    quantity = int(input(f"Enter Quantity of Product: "))
    products.append((name, price, quantity))

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
