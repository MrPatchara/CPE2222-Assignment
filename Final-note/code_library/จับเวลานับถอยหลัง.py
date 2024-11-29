#โปรแกรมจับเวลานับถอยหลังสำหรับจำนวนวินาทีที่กำหนด
import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"เวลาที่เหลือ: {seconds} วินาที")
        time.sleep(1)
        seconds -= 1
    print("หมดเวลา!")

# รับข้อมูลจากผู้ใช้
seconds = int(input("ใส่เวลานับถอยหลัง (วินาที): "))
countdown_timer(seconds)