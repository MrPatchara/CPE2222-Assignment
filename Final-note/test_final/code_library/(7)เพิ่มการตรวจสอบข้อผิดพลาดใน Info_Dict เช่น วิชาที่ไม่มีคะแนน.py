# โปรแกรมตรวจสอบคะแนนของนักเรียนที่เรียนวิชาที่มีในระบบ
from module_exam import Info_Dict, grading

# รายวิชาที่มีในระบบ
valid_subjects = ['Mathematics', 'Physics', 'English', 'Chemistry', 'Computer']

def validate_scores(info_dict, valid_subjects):
    """ตรวจสอบว่าทุกวิชามีคะแนนครบในระบบ"""
    errors = []
    for student_id, scores in info_dict.items():
        for subject in valid_subjects:
            if subject not in scores:
                errors.append(f"Missing score for {subject} in student ID {student_id}")
    return errors

print("----------------------------------------------------------")
errors = validate_scores(Info_Dict, valid_subjects)
if errors:
    print("Errors found in the data:")
    for error in errors:
        print(f"  - {error}")
else:
    print("All data is valid.")
print("----------------------------------------------------------\n")