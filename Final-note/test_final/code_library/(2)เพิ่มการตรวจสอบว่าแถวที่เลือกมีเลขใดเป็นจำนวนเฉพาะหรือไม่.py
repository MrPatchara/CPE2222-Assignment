# โปรแกรมนี้สร้างแถวตัวเลขแบบสะสม และเพิ่มการตรวจสอบว่าแถวที่เลือกมีเลขใดเป็นจำนวนเฉพาะหรือไม่
# สามารถเลือกแถวที่ต้องการดูได้ และออกจากโปรแกรมเมื่อป้อน -1
def generate_rows(num_rows):
    rows = [[1]]
    for i in range(1, num_rows + 1):
        previous_row = rows[-1]
        new_row = [previous_row[-1]]
        for j in range(len(previous_row)):
            new_row.append(new_row[-1] + previous_row[j])
        rows.append(new_row)
    return rows

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    rows = []
    while True:
        try:
            user_row = int(input("Please Enter Degree : "))
            if user_row == -1:
                print("ออกจากโปรแกรม")
                break
            if user_row < 0:
                print("กรุณากรอกหมายเลขแถวที่เป็นค่าบวกหรือศูนย์")
                continue
            if len(rows) <= user_row:
                rows = generate_rows(user_row)
            primes = [x for x in rows[user_row] if is_prime(x)]
            print(f"Row {user_row}: {rows[user_row]} (Prime Numbers: {primes})\n")
        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()