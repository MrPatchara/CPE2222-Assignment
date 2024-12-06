# โปรแกรมจัดการข้อมูลสินค้าในคลัง
#เพื่อเพิ่มความซับซ้อนและประยุกต์โค้ดมากขึ้นสำหรับการฝึกซ้อม ผมจะปรับโค้ดโดยเพิ่มฟังก์ชันที่ช่วยลดการเขียนซ้ำ เพิ่มการคำนวณเพิ่มเติม และเพิ่มคุณสมบัติในการจัดการข้อมูล เช่น การแสดงข้อมูลรวม การคำนวณราคา รวมถึงการจัดการข้อผิดพลาดในการป้อนข้อมูล
def get_product_info(index):
    #รับข้อมูลสินค้าแต่ละชิ้นจากผู้ใช้
    #- index: ลำดับที่ของสินค้า
    #- คืนค่า (product, price, quantity)

    while True:  # ใช้ loop เพื่อให้ผู้ใช้กรอกข้อมูลใหม่ในกรณีที่มีข้อผิดพลาด
        try:
            product = str(input(f'Enter the name of product {index}: '))  # ชื่อสินค้า
            price = float(input(f'Enter the price of product {index}: '))  # ราคาสินค้า
            quantity = int(input(f'Enter the quantity of product {index}: '))  # จำนวนสินค้า
            if price < 0 or quantity < 0:  # ตรวจสอบว่าราคาและจำนวนต้องไม่ติดลบ
                raise ValueError("Price and quantity must be non-negative.")
            return product, price, quantity  # คืนค่าข้อมูลเมื่อไม่มีข้อผิดพลาด
        except ValueError as e:
            # แสดงข้อความข้อผิดพลาดและให้กรอกข้อมูลใหม่
            print(f"Invalid input: {e}. Please try again.")

def display_inventory(products):
    #แสดงตารางสินค้าในคลัง พร้อมรวมยอดทั้งหมด
    #- products: รายการสินค้าที่เป็น list ของ (product, price, quantity)
    # กำหนดความกว้างของคอลัมน์ในตาราง
    width_product = 25
    width_price = 10
    width_quantity = 15
    width_total = 10

    # พิมพ์หัวตาราง
    print('-' * 65)
    print('                     Inventory                     ')
    print('-' * 65)
    print(f"{'Item':<{width_product}}{'Price':>{width_price}}{'Quantity':>{width_quantity}}{'Total':>{width_total}}")
    print('-' * 65)

    # ตัวแปรสำหรับเก็บผลรวม
    grand_total = 0  # ยอดรวมราคาสินค้าทั้งหมด
    total_quantity = 0  # ยอดรวมจำนวนสินค้าทั้งหมด

    # แสดงข้อมูลสินค้าแต่ละชิ้น
    for product, price, quantity in products:
        total = price * quantity  # คำนวณราคาสินค้ารวม (ราคา * จำนวน)
        grand_total += total  # เพิ่มยอดรวมสินค้าลงใน grand_total
        total_quantity += quantity  # เพิ่มจำนวนสินค้าใน total_quantity
        # พิมพ์ข้อมูลสินค้าแต่ละชิ้นในตาราง
        print(f"{product:<{width_product}}{price:>{width_price}.2f}{quantity:>{width_quantity}}{total:>{width_total}.2f}")
    
    # แสดงผลรวมทั้งหมด
    print('-' * 65)
    print(f"{'Total Quantity':<{width_product}}{'':>{width_price + width_quantity}}{total_quantity:>{width_total}}")
    print(f"{'Grand Total':<{width_product}}{'':>{width_price + width_quantity}}{grand_total:>{width_total}.2f}")
    print('-' * 65)

def main():
    #โปรแกรมหลักสำหรับจัดการข้อมูลสินค้าในคลัง
    print("Welcome to the Inventory Management System!")  # ข้อความต้อนรับ
    products = []  # รายการเก็บข้อมูลสินค้า
    for i in range(1, 4):  # ใช้ loop เพื่อขอข้อมูลสินค้า 3 ชิ้น (สามารถเพิ่มจำนวนได้ง่าย)
        products.append(get_product_info(i))  # เก็บข้อมูลสินค้าใน list
    
    display_inventory(products)  # เรียกฟังก์ชันแสดงตารางสินค้า

# เรียกใช้งานโปรแกรมหลัก
main()
