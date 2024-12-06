# โปรแกรมแสดงกราฟแท่งแสดงการกระจายของเกรดของนักเรียนในรายวิชาที่เลือก
from module_exam import Info_Dict, grading
import matplotlib.pyplot as plt

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

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        grade = grading(subject, score)
        grades_count[grade] += 1

    grades = list(grades_count.keys())
    counts = list(grades_count.values())

    plt.bar(grades, counts, color='blue')
    plt.title(f"Grade Distribution for {subject}")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.show()

    print("----------------------------------------------------------\n")