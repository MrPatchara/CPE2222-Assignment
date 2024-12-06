# โปรแกรมแสดงผลคะแนนและเกรดของนักเรียนในรายวิชาต่างๆ
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
    student_scores = []

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        grade = grading(subject, score)
        student_scores.append((student_id, score, grade))

    # เรียงลำดับคะแนนจากสูงไปต่ำ
    student_scores.sort(key=lambda x: x[1], reverse=True)

    print(f"{'Student ID':<15}{'Score':<10}{'Grade':<10}")
    for student_id, score, grade in student_scores:
        print(f"{student_id:<15}{score:<10}{grade:<10}")

    print("----------------------------------------------------------\n")