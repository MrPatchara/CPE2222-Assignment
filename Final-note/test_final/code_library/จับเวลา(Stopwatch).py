#โปรแกรมจับเวลาพื้นฐานที่สามารถเริ่มและหยุดได้
import time

def stopwatch():
    input("กด Enter เพื่อเริ่มจับเวลา")
    start_time = time.time()
    input("กด Enter เพื่อหยุดจับเวลา")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"เวลาที่ผ่านไป: {elapsed_time:.2f} วินาที")

# ตัวอย่างการใช้งาน
stopwatch()
