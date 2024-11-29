#8.จงเขียนโปรแกรมในการจัดตารางทำงานของพนักงานรักษาความปลอดภัย (รปภ.) จำนวน 5 คน ในโรงงานแห่งหนึ่ง โดย รปภ. มีนามสมมุติเป็น “A”, “B”, “C”, “D” และ “E”

import random

# รายชื่อพนักงาน รปภ.
security_guards = ["A", "B", "C", "D", "E"]

# ค่าจ้าง
morning_rate = 200
afternoon_rate = 150

# ตารางงาน
schedule = {
    "Monday": ["", ""],
    "Tuesday": ["", ""],
    "Wednesday": ["", ""],
    "Thursday": ["", ""],
    "Friday": ["", ""]
}

# ฟังก์ชันสุ่มการทำงาน
def generate_schedule():
    # สุ่ม รปภ. สำหรับแต่ละวัน
    for day in schedule:
        # สุ่มคนทำงานรอบเช้าและรอบบ่าย
        morning_guard = random.choice(security_guards)
        afternoon_guard = random.choice(security_guards)
        
        # ตรวจสอบว่ารปภ. คนเดียวกันไม่ทำงานซ้ำในวันเดียวกัน
        while morning_guard == afternoon_guard:
            afternoon_guard = random.choice(security_guards)
        
        schedule[day][0] = morning_guard
        schedule[day][1] = afternoon_guard

# ฟังก์ชันคำนวณค่าจ้าง
def calculate_income():
    income = {guard: 0 for guard in security_guards}
    
    # คำนวณค่าจ้าง
    for day in schedule:
        morning_guard, afternoon_guard = schedule[day]
        income[morning_guard] += morning_rate
        income[afternoon_guard] += afternoon_rate
    
    return income

# ฟังก์ชันแสดงตารางทำงานแบบฟอร์แมตใหม่
def print_schedule():
    print("-"*49)
    print(f"{'':<15} | {'8:00 - 12:00':<12}  | {'13:00 - 17:00':<12} |")
    print("-"*49)
    
    for day in schedule:
        morning_guard, afternoon_guard = schedule[day]
        print(f"{day:<15} | {morning_guard:^12}  |  {afternoon_guard:^12} |")
        print("-"*49)
    
    print("\n----------------------------------")
    print("          Income Summary")
    print("----------------------------------")
    for guard, amount in income.items():
        print(f'"{guard}" earns {amount} $Bath for this week\n')

# สร้างตารางงานและคำนวณค่าจ้าง
generate_schedule()
income = calculate_income()

# แสดงตารางงานและสรุปค่าจ้าง
print_schedule()
