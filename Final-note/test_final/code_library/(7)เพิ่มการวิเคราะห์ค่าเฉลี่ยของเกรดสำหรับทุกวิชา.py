# โปรแกรมแสดงค่าเฉลี่ยของคะแนนของนักเรียนในแต่ละวิชา
from module_exam import Info_Dict, grading

# รายวิชาที่มีในระบบ
valid_subjects = ['Mathematics', 'Physics', 'English', 'Chemistry', 'Computer']

print("----------------------------------------------------------")
for subject in valid_subjects:
    grades_count = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
    total_score = 0

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        grade = grading(subject, score)
        grades_count[grade] += 1
        total_score += score

    average_score = total_score / len(Info_Dict)
    print(f"{subject}: Average Score = {average_score:.2f}")
print("----------------------------------------------------------\n")