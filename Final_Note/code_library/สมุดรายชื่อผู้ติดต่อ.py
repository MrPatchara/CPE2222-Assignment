#โปรแกรมเพิ่ม ลบ และค้นหาผู้ติดต่อในสมุดรายชื่อ
def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"เพิ่มผู้ติดต่อ: {name} - {phone}")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"ลบผู้ติดต่อ: {name}")
    else:
        print(f"ไม่พบผู้ติดต่อชื่อ {name}")


def search_contact(contacts, name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"ไม่พบผู้ติดต่อชื่อ {name}")

# ตัวอย่างการใช้งาน
contacts = {}
while True:
    print("\n1. เพิ่มผู้ติดต่อ")
    print("2. ลบผู้ติดต่อ")
    print("3. ค้นหาผู้ติดต่อ")
    print("4. แสดงรายชื่อทั้งหมด")
    print("5. ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    
    if choice == '1':
        name = input("ใส่ชื่อ: ")
        phone = input("ใส่เบอร์โทร: ")
        add_contact(contacts, name, phone)
    elif choice == '2':
        name = input("ใส่ชื่อผู้ติดต่อที่ต้องการลบ: ")
        delete_contact(contacts, name)
    elif choice == '3':
        name = input("ใส่ชื่อผู้ติดต่อที่ต้องการค้นหา: ")
        search_contact(contacts, name)
    elif choice == '4':
        print("รายชื่อผู้ติดต่อทั้งหมด:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '5':
        print("ออกจากโปรแกรม")
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง")