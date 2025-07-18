from db_config import connect

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female/Other): ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO students (name, age, gender, course, marks) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (name, age, gender, course, marks))
    db.commit()
    print("✅ Student added successfully.")
    db.close()

def view_students():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    print("\n📋 All Students:")
    for row in results:
        print(row)
    db.close()

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    db.commit()
    print("🗑️ Student deleted and logged.")
    db.close()

def search_student():
    keyword = input("Enter name or ID to search: ")

    db = connect()
    cursor = db.cursor()

    if keyword.isdigit():
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (int(keyword),))
    else:
        cursor.execute("SELECT * FROM students WHERE name LIKE %s", ('%' + keyword + '%',))

    results = cursor.fetchall()
    print("\n🔍 Search Results:")
    for row in results:
        print(row)
    db.close()

def main():
    while True:
        print("\n🔸 Student Records Management System 🔸")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
