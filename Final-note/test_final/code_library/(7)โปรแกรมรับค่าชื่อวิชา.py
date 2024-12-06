# โปรแกรมหาค่าเฉลี่ยคะแนนและจำนวนนักเรียนในแต่ละเกรดของรายวิชาที่เลือก
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
    grades_count = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
    total_score = 0

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        grade = grading(subject, score)
        grades_count[grade] += 1
        total_score += score

    total_students = len(Info_Dict)
    print(f"{'Grade':<10}{'A number of students (Percentage)':<30}")
    for grade, count in grades_count.items():
        percentage = (count / total_students) * 100
        print(f"  {grade:<17}{count:>2} ({percentage:>5.2f})")

    average_score = total_score / total_students
    print("----------------------------------------------------------")
    print(f"  Average Score = {average_score:.2f}")
    print("----------------------------------------------------------\n")