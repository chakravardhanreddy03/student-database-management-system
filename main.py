import sqlite3

def add_student(id, name, branch, year, cgpa):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
        (id, name, branch, year, cgpa)
    )

    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    for student in cursor.fetchall():
        print(student)

    conn.close()

def search_student(student_id):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    print(cursor.fetchone())

    conn.close()

def update_student(student_id, new_cgpa):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET cgpa=? WHERE id=?",
        (new_cgpa, student_id)
    )

    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = int(input("Enter Year: "))
        cgpa = float(input("Enter CGPA: "))

        add_student(id, name, branch, year, cgpa)
        print("Student Added Successfully")

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        search_student(student_id)

    elif choice == "4":
        student_id = int(input("Enter Student ID: "))
        new_cgpa = float(input("Enter New CGPA: "))
        update_student(student_id, new_cgpa)

    elif choice == "5":
        student_id = int(input("Enter Student ID: "))
        delete_student(student_id)

    elif choice == "6":
        break