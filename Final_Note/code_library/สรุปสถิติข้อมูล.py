#โปรแกรมคำนวณค่าเฉลี่ย มัธยฐาน และฐานนิยมของชุดข้อมูล
import statistics

def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    return mean, median, mode

# รับข้อมูลจากผู้ใช้
data = list(map(float, input("ใส่ข้อมูลตัวเลข (คั่นด้วยช่องว่าง): ").split()))
mean, median, mode = calculate_statistics(data)
print(f"ค่าเฉลี่ย: {mean:.2f}, มัธยฐาน: {median:.2f}, ฐานนิยม: {mode:.2f}")