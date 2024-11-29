def sort_students_by_score(students):
    # จัดเรียงตามคะแนนจากมากไปน้อย
    return sorted(students, key=lambda x: x['score'], reverse=True)

# ข้อมูลนักเรียนตัวอย่าง
students = [
    {"name": "สมชาย", "score": 85},
    {"name": "สมหญิง", "score": 92},
    {"name": "จันทร์", "score": 78},
    {"name": "เพ็ญ", "score": 88}
]

sorted_students = sort_students_by_score(students)
print("ข้อมูลนักเรียนหลังจัดเรียง:")
for student in sorted_students:
    print(f"{student['name']}: {student['score']} คะแนน")