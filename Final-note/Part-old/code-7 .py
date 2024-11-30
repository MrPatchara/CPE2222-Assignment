#7.กำหนดให้ แฟ้มข้อมูลชื่อ “module_exam.py” ประกอบข้อมูลแบบพจนานุกรมซ้อนพจนานุกรม (Nested Dictionary) ชื่อ “Info_Dict” และฟังก็ชัน (Function) ชื่อ “grading”

# โปรแกรมหลักที่เชื่อมต่อกับ module_exam.py
import module_exam  # นำเข้าข้อมูลจากแฟ้ม module_exam.py

# ฟังก์ชันหลักในการประมวลผลข้อมูลและแสดงผล
def process_grading(subject):
    # ตรวจสอบชื่อวิชา
    valid_subjects = ['Mathematics', 'Physics', 'English', 'Chemistry', 'Computer']
    if subject not in valid_subjects:
        print("!!! Subject Error !!!")
        print("-"*50, "\n")
        return

    grade_count = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
    total_score = 0
    total_students = len(module_exam.Info_Dict)

    # ประมวลผลข้อมูลของนักศึกษาทุกคน
    for student_id, scores in module_exam.Info_Dict.items():
        score = scores[subject]
        grade = module_exam.grading(subject, score)
        grade_count[grade] += 1
        total_score += score

    # คำนวณผลคะแนนเฉลี่ย
    average_score = total_score / total_students

    # แสดงผลการคำนวณ
    print(f"{'Grade':<10}{'A number of students (Percentage)':<40}")
    for grade, count in grade_count.items():
        percentage = (count / total_students) * 100
        print(f"{"  "}{grade:<10}{"        "}{count}{" "}({percentage:.2f})")
    print("-"*50)
    print(f"            Average Score = {average_score:.2f}")
    print("-"*50, "\n")

# รับค่าและเรียกใช้ฟังก์ชัน
if __name__ == "__main__":
    subject = input("Enter subject [Mathematics, Physics, English, Chemistry, Computer]: ")
    print("-"*50)
    process_grading(subject)
