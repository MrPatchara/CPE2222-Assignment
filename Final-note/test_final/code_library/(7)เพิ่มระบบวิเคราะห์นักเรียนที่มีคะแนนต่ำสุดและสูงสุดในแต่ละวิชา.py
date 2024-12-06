# โปรแกรมแสดงผลรายชื่อนักเรียนที่ได้คะแนนสูงสุดและต่ำสุดของแต่ละวิชา
from module_exam import Info_Dict, grading

# รายวิชาที่มีในระบบ
valid_subjects = ['Mathematics', 'Physics', 'English', 'Chemistry', 'Computer']

print("----------------------------------------------------------")
for subject in valid_subjects:
    max_score = -1
    min_score = 101
    top_student = ""
    low_student = ""

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        if score > max_score:
            max_score = score
            top_student = student_id
        if score < min_score:
            min_score = score
            low_student = student_id

    print(f"{subject}:")
    print(f"  Top Student: {top_student} with Score = {max_score}")
    print(f"  Lowest Student: {low_student} with Score = {min_score}")
    print("----------------------------------------------------------\n")