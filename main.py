# Load students from file
try:
    students = []

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            student = {
                "id": data[0],
                "name": data[1],
                "marks": data[2],
                "attendance": data[3]
            }

            students.append(student)

except FileNotFoundError:
    students = []

# Save data to file
def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                f"{student['id']},"
                f"{student['name']},"
                f"{student['marks']},"
                f"{student['attendance']}\n"
            )


# Add student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    attendance = input("Enter Attendance (%): ")

    student = {
        "id": student_id,
        "name": name,
        "marks": marks,
        "attendance": attendance
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


# View students
def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        print("\nStudent List:")
        for student in students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Marks: {student['marks']} | "
                f"Attendance: {student['attendance']}%"
            )

#Sort Students in Alphabetically
def sort_students():
    students.sort(key=lambda x: x["name"])

    print("\nStudents sorted alphabetically!")

    view_students()

# Delete student
def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"] == name:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found")

# Search student
def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"] == name:
            print(
                f"\nID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Marks: {student['marks']} | "
                f"Attendance: {student['attendance']}%"
            )
            return

    print("Student not found")

# Update student
def update_student():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"] == name:

            student["name"] = input("Enter new name: ")
            student["marks"] = input("Enter new marks: ")
            student["attendance"] = input("Enter new attendance: ")

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found")

# Main program
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Sort Students")

    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        update_student()

    
    elif choice == "6":
        sort_students()

    elif choice == "7":
        print("Thank you!")

        break




        

    else:
        print("Invalid choice")