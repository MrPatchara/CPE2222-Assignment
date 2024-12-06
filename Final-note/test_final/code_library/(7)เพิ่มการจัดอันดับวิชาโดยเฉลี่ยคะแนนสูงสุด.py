# โปรแกรมแสดงผลลัพธ์ของการทำงานของโมดูล module_exam.py
from module_exam import Info_Dict, grading

# รายวิชาที่มีในระบบ
valid_subjects = ['Mathematics', 'Physics', 'English', 'Chemistry', 'Computer']

print("----------------------------------------------------------")
subject_scores = {}

for subject in valid_subjects:
    grades_count = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}
    total_score = 0

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        grade = grading(subject, score)
        grades_count[grade] += 1
        total_score += score

    average_score = total_score / len(Info_Dict)
    subject_scores[subject] = average_score

sorted_subjects = sorted(subject_scores.items(), key=lambda x: x[1], reverse=True)

print("Subject Ranking by Average Score:")
for rank, (subject, avg_score) in enumerate(sorted_subjects, start=1):
    print(f"{rank}. {subject} - Average Score: {avg_score:.2f}")
print("----------------------------------------------------------\n")