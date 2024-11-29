import sqlite3

# ========================= Database Setup ========================= #
def setup_database():
    #ตั้งค่าฐานข้อมูล SQLite
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # ตารางนักเรียน
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade_level TEXT NOT NULL
        )
    ''')

    # ตารางครู
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')

    # ตารางวิชา
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            teacher_id INTEGER NOT NULL,
            max_seats INTEGER NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')

    # ตารางลงทะเบียนเรียน
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            grade REAL,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    ''')

    conn.commit()
    conn.close()

# ========================= CRUD Functions ========================= #
def add_student(name, age, grade_level):
    #เพิ่มนักเรียนใหม่
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade_level) VALUES (?, ?, ?)", (name, age, grade_level))
    conn.commit()
    conn.close()
    print(f"Student '{name}' added successfully.")

def add_teacher(name, subject):
    #เพิ่มครูใหม่
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (name, subject) VALUES (?, ?)", (name, subject))
    conn.commit()
    conn.close()
    print(f"Teacher '{name}' added successfully.")

def add_subject(name, teacher_id, max_seats):
    #เพิ่มวิชาใหม่
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subjects (name, teacher_id, max_seats) VALUES (?, ?, ?)", (name, teacher_id, max_seats))
    conn.commit()
    conn.close()
    print(f"Subject '{name}' added successfully.")

# ========================= Enrollment Management ========================= #
def enroll_student(student_id, subject_id):
    #ลงทะเบียนนักเรียนในวิชา
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # ตรวจสอบว่าวิชานี้เต็มหรือยัง
    cursor.execute("SELECT COUNT(*) FROM enrollments WHERE subject_id = ?", (subject_id,))
    current_enrollments = cursor.fetchone()[0]

    cursor.execute("SELECT max_seats FROM subjects WHERE id = ?", (subject_id,))
    max_seats = cursor.fetchone()

    if not max_seats:
        print("Subject does not exist.")
        conn.close()
        return

    if current_enrollments < max_seats[0]:
        cursor.execute("INSERT INTO enrollments (student_id, subject_id, grade) VALUES (?, ?, NULL)", (student_id, subject_id))
        conn.commit()
        print("Enrollment successful.")
    else:
        print("Subject is full.")

    conn.close()

def assign_grade(student_id, subject_id, grade):
    #ใส่เกรดให้กับนักเรียน
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE enrollments SET grade = ? WHERE student_id = ? AND subject_id = ?", (grade, student_id, subject_id))
    conn.commit()
    conn.close()
    print("Grade assigned successfully.")

# ========================= Reporting ========================= #
def view_student_report(student_id):
    #แสดงรายงานผลการเรียนของนักเรียน
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.name, sub.name, e.grade 
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN subjects sub ON e.subject_id = sub.id
        WHERE s.id = ?
    ''', (student_id,))
    report = cursor.fetchall()
    conn.close()

    if report:
        print(f"{'Student Name':<20}{'Subject':<20}{'Grade':<10}")
        print('-' * 50)
        for row in report:
            print(f"{row[0]:<20}{row[1]:<20}{row[2] if row[2] is not None else 'Not Assigned':<10}")
    else:
        print("No report found for this student.")

# ========================= Main Menu ========================= #
def main():
    setup_database()
    print("Welcome to the School Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Subject")
        print("4. Enroll Student in Subject")
        print("5. Assign Grade")
        print("6. View Student Report")
        print("7. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade_level = input("Enter grade level: ")
            add_student(name, age, grade_level)
        elif choice == '2':
            name = input("Enter teacher name: ")
            subject = input("Enter subject taught: ")
            add_teacher(name, subject)
        elif choice == '3':
            name = input("Enter subject name: ")
            teacher_id = int(input("Enter teacher ID: "))
            max_seats = int(input("Enter maximum seats: "))
            add_subject(name, teacher_id, max_seats)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            subject_id = int(input("Enter subject ID: "))
            enroll_student(student_id, subject_id)
        elif choice == '5':
            student_id = int(input("Enter student ID: "))
            subject_id = int(input("Enter subject ID: "))
            grade = float(input("Enter grade: "))
            assign_grade(student_id, subject_id, grade)
        elif choice == '6':
            student_id = int(input("Enter student ID: "))
            view_student_report(student_id)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# ========================= Start the Program ========================= #
main()
