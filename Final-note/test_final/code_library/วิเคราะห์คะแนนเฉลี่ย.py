# โปรแกรมคำนวณค่าเฉลี่ยคะแนน และหาคะแนนสูงสุดและต่ำสุดจากคะแนนที่ผู้ใช้ใส่เข้ามา
def calculate_average(scores):
    # คำนวณค่าเฉลี่ย
    return sum(scores) / len(scores)


def find_highest_and_lowest(scores):
    # หาค่าคะแนนสูงสุดและต่ำสุด
    return max(scores), min(scores)


# รับข้อมูลคะแนนจากผู้ใช้
scores = list(map(float, input("ใส่คะแนนที่ได้รับ (คั่นด้วยช่องว่าง): ").split()))


# คำนวณและแสดงผล
average = calculate_average(scores)
highest, lowest = find_highest_and_lowest(scores)
print(f"ค่าเฉลี่ย: {average:.2f}, สูงสุด: {highest}, ต่ำสุด: {lowest}")
