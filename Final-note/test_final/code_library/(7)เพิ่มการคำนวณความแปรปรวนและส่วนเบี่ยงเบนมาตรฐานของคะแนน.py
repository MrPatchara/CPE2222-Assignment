# โปรแกรมคำนวณคะแนนเฉลี่ย ความแปรปรวน และส่วนเบี่ยงเบนมาตรฐานของรายวิชาที่เลือก
from module_exam import Info_Dict, grading
import math

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
    total_score = 0
    scores_list = []

    for student_id, scores in Info_Dict.items():
        score = scores[subject]
        scores_list.append(score)
        total_score += score

    average_score = total_score / len(scores_list)
    variance = sum((x - average_score) ** 2 for x in scores_list) / len(scores_list)
    std_deviation = math.sqrt(variance)

    print(f"  Average Score          = {average_score:.2f}")
    print(f"  Variance of Scores     = {variance:.2f}")
    print(f"  Standard Deviation     = {std_deviation:.2f}")
    print("----------------------------------------------------------\n")