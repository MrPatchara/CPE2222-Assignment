# โปรแกรมแสดงผลการจัดกลุ่มนักเรียนตามเกรดของรายวิชาที่เลือก
from module_exam import Info_Dict, grading

# รายวิชาที่มีในระบบ
valid_subjects = ['Mathematics', 'Physics', 'English', 'Chemistry', 'Computer']

print("----------------------------------------------------------")
subject = input("Enter your subject [Mathematics, Physics, English, Chemistry, Computer]: ")

if subject not in valid_subjects:
    print("----------------------------------------------------------")
    print("!!!   Subject Error   !!!")
    print("----------------------------------------------------------\n")
else:
    print("----------------------------------------------------------")
    grouped_students = {'A': [], 'B+': [], 'B': [], 'C+': [], 'C': [], 'D+': [], 'D': [], 'F': []}

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        grade = grading(subject, score)
        grouped_students[grade].append(student_id)

    print("Students Grouped by Grades:")
    for grade, students in grouped_students.items():
        print(f"  {grade}: {', '.join(students) if students else 'No students'}")

    print("----------------------------------------------------------\n")