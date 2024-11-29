#โปรแกรมเพิ่ม, ลบ และแสดงรายการ To-Do List
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"เพิ่มงาน: {task}")

def remove_task(todo_list, task_index):
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"ลบงาน: {removed_task}")
    else:
        print("หมายเลขงานไม่ถูกต้อง")

def display_tasks(todo_list):
    print("รายการ To-Do List:")
    if not todo_list:
        print("ไม่มีงานในรายการ")
    for i, task in enumerate(todo_list):
        print(f"{i}. {task}")

# ตัวอย่างการใช้งาน
todo_list = []
while True:
    print("\n1. เพิ่มงาน")
    print("2. ลบงาน")
    print("3. แสดงรายการ")
    print("4. ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    
    if choice == '1':
        task = input("ใส่ชื่องาน: ")
        add_task(todo_list, task)
    elif choice == '2':
        task_index = int(input("ใส่หมายเลขงานที่ต้องการลบ: "))
        remove_task(todo_list, task_index)
    elif choice == '3':
        display_tasks(todo_list)
    elif choice == '4':
        print("ออกจากโปรแกรม")
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง")