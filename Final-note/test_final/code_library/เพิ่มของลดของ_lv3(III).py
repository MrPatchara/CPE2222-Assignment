# โปรแกรมจัดการธุรกิจ
import sqlite3
from datetime import datetime

# ========================= Database Setup ========================= #
def setup_database():
    #ตั้งค่าฐานข้อมูล SQLite
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()

    # ตารางสินค้า
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    # ตารางคำสั่งซื้อ
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            total REAL NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    # รายละเอียดคำสั่งซื้อ
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_name TEXT,
            quantity INTEGER,
            price REAL,
            FOREIGN KEY (order_id) REFERENCES orders(id)
        )
    ''')

    conn.commit()
    conn.close()

# ========================= CRUD Functions ========================= #
def add_product(name, price, quantity):
    #เพิ่มสินค้าใหม่
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
        conn.commit()
        print(f"Product '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Product '{name}' already exists.")
    finally:
        conn.close()

def view_products():
    #แสดงรายการสินค้า
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()

    if products:
        print(f"{'ID':<5}{'Name':<20}{'Price':<10}{'Quantity':<10}")
        print('-' * 45)
        for product in products:
            print(f"{product[0]:<5}{product[1]:<20}{product[2]:<10.2f}{product[3]:<10}")
    else:
        print("No products available.")

def update_stock(product_name, quantity_sold):
    #ลดจำนวนสต็อกสินค้าหลังการขาย
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM products WHERE name = ?", (product_name,))
    result = cursor.fetchone()

    if result and result[0] >= quantity_sold:
        cursor.execute("UPDATE products SET quantity = quantity - ? WHERE name = ?", (quantity_sold, product_name))
        conn.commit()
        print(f"Stock updated for '{product_name}'.")
    else:
        print(f"Not enough stock for '{product_name}'.")
    conn.close()

# ========================= Order Management ========================= #
def create_order(customer_name, items):
    #สร้างคำสั่งซื้อใหม่
    #param customer_name: ชื่อลูกค้า
    #param items: รายการสินค้า {ชื่อสินค้า: จำนวน}
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()

    total = 0
    for product_name, quantity in items.items():
        cursor.execute("SELECT price, quantity FROM products WHERE name = ?", (product_name,))
        product = cursor.fetchone()
        if not product:
            print(f"Product '{product_name}' does not exist.")
            conn.close()
            return
        elif product[1] < quantity:
            print(f"Not enough stock for '{product_name}'.")
            conn.close()
            return
        total += product[0] * quantity

    # สร้างคำสั่งซื้อใหม่
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO orders (customer_name, total, date) VALUES (?, ?, ?)", (customer_name, total, order_date))
    order_id = cursor.lastrowid

    # เพิ่มรายละเอียดคำสั่งซื้อ
    for product_name, quantity in items.items():
        cursor.execute("SELECT price FROM products WHERE name = ?", (product_name,))
        price = cursor.fetchone()[0]
        cursor.execute("INSERT INTO order_details (order_id, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                       (order_id, product_name, quantity, price))
        # ลดจำนวนสต็อกสินค้า
        update_stock(product_name, quantity)

    conn.commit()
    print(f"Order created successfully for {customer_name}. Total: {total:.2f}")
    conn.close()

def view_orders():
    #ดูคำสั่งซื้อทั้งหมด
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()

    if orders:
        print(f"{'ID':<5}{'Customer':<20}{'Total':<10}{'Date':<20}")
        print('-' * 55)
        for order in orders:
            print(f"{order[0]:<5}{order[1]:<20}{order[2]:<10.2f}{order[3]:<20}")
    else:
        print("No orders available.")

# ========================= Main Menu ========================= #
def main():
    setup_database()
    print("Welcome to the Business Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Create Order")
        print("4. View Orders")
        print("5. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(name, price, quantity)
        elif choice == '2':
            view_products()
        elif choice == '3':
            customer_name = input("Enter customer name: ")
            items = {}
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                quantity = int(input(f"Enter quantity for '{product_name}': "))
                items[product_name] = quantity
            create_order(customer_name, items)
        elif choice == '4':
            view_orders()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# ========================= Start the Program ========================= #
main()
