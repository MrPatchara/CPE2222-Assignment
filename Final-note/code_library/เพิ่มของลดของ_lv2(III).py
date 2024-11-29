import csv

def get_product_info():
    #รับข้อมูลสินค้าแต่ละชิ้นจากผู้ใช้
    #- คืนค่า dictionary {ชื่อสินค้า: (ราคา, จำนวน)}
    while True:
        try:
            product_name = str(input("Enter the product name: ")).strip()
            if not product_name:
                raise ValueError("Product name cannot be empty.")
            
            price = float(input("Enter the price of the product: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            quantity = int(input("Enter the quantity of the product: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            
            return product_name, price, quantity
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def display_inventory(products):
    #แสดงตารางสินค้าในคลัง พร้อมคำนวณยอดรวม ราคาหลังส่วนลด และภาษี
    width_product = 25
    width_price = 10
    width_quantity = 10
    width_total = 15
    width_discount = 10
    width_tax = 10

    print('-' * 80)
    print('                     Inventory Report                    ')
    print('-' * 80)
    print(f"{'Item':<{width_product}}{'Price':>{width_price}}{'Quantity':>{width_quantity}}{'Subtotal':>{width_total}}{'Discount':>{width_discount}}{'Tax':>{width_tax}}")
    print('-' * 80)

    grand_total = 0
    for product, (price, quantity) in products.items():
        subtotal = price * quantity
        discount = 0.1 * subtotal if quantity >= 10 else 0  # ส่วนลด 10% หากซื้อเกิน 10 ชิ้น
        tax = 0.07 * (subtotal - discount)  # ภาษี 7%
        total = subtotal - discount + tax
        grand_total += total
        
        print(f"{product:<{width_product}}{price:>{width_price}.2f}{quantity:>{width_quantity}}{subtotal:>{width_total}.2f}{discount:>{width_discount}.2f}{tax:>{width_tax}.2f}")

    print('-' * 80)
    print(f"{'Grand Total':<{width_product}}{'':>{width_price + width_quantity + width_total}}{grand_total:>{width_tax + width_discount + 10}.2f}")
    print('-' * 80)

def save_to_csv(products, filename="inventory_report.csv"):
    #บันทึกรายงานสินค้าในคลังลงไฟล์ CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Price", "Quantity", "Subtotal", "Discount", "Tax", "Total"])
        
        for product, (price, quantity) in products.items():
            subtotal = price * quantity
            discount = 0.1 * subtotal if quantity >= 10 else 0
            tax = 0.07 * (subtotal - discount)
            total = subtotal - discount + tax
            writer.writerow([product, price, quantity, subtotal, discount, tax, total])
    print(f"Inventory report saved to {filename}")

def main():
    #โปรแกรมหลัก
    print("Welcome to the Advanced Inventory Management System!")
    products = {}

    while True:
        action = input("Enter 'add' to add a product, 'view' to display inventory, 'save' to save to CSV, or 'quit' to exit: ").lower()
        if action == 'add':
            product_name, price, quantity = get_product_info()
            if product_name in products:
                # หากสินค้ามีอยู่แล้ว จะอัปเดตจำนวนสินค้า
                existing_price, existing_quantity = products[product_name]
                if price != existing_price:
                    print(f"Warning: Price for {product_name} is updated from {existing_price:.2f} to {price:.2f}.")
                products[product_name] = (price, existing_quantity + quantity)
            else:
                products[product_name] = (price, quantity)
        elif action == 'view':
            if products:
                display_inventory(products)
            else:
                print("No products in inventory yet.")
        elif action == 'save':
            if products:
                save_to_csv(products)
            else:
                print("No products to save.")
        elif action == 'quit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

# เรียกใช้งานโปรแกรม
main()
