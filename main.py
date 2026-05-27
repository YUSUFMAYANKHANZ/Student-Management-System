# Student Management System
# Author: Yusuf
## Built a Student Management System with CRUD operations,sorting,
#  validation, and persistent file storage using Python. 
 

# Load students from file
try:
    students = []

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                student = {
                    "id": data[0],
                    "name": data[1],
                    "marks": data[2],
                    "attendance": data[3]
                }

                students.append(student)

except FileNotFoundError:
    students = []


# Save students
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

    # Prevent duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists")
            return

    name = input("Enter Student Name: ")

    marks = int(input("Enter Marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    attendance = int(input("Enter Attendance (0-100): "))
    if attendance < 0 or attendance > 100:
        print("Invalid attendance")
        return

    student = {
        "id": student_id,
        "name": name,
        "marks": str(marks),
        "attendance": str(attendance)
    }

    students.append(student)

    save_students()

    print("Student added successfully!")


# View students
def view_students():

    if len(students) == 0:
        print("No students found")

    else:

        print("\n===== Student List =====")

        for student in students:

            print(
                f"ID:{student['id']} | "
                f"Name:{student['name']} | "
                f"Marks:{student['marks']} | "
                f"Attendance:{student['attendance']}%"
            )


# Delete student
def delete_student():

    name = input("Enter student name: ")

    for student in students:

        if student["name"] == name:

            students.remove(student)

            save_students()

            print("Student deleted successfully")

            return

    print("Student not found")


# Search student
def search_student():

    name = input("Enter student name: ")

    for student in students:

        if student["name"] == name:

            print(
                f"\nID:{student['id']} | "
                f"Name:{student['name']} | "
                f"Marks:{student['marks']} | "
                f"Attendance:{student['attendance']}%"
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

            student["attendance"] = input(
                "Enter new attendance: "
            )

            save_students()

            print("Student updated successfully")

            return

    print("Student not found")


# Sort alphabetically
def sort_students():

    students.sort(
        key=lambda x: x["name"]
    )

    print("\nSorted alphabetically")

    view_students()


# Sort by marks
def sort_by_marks():

    students.sort(
        key=lambda x: int(x["marks"]),
        reverse=True
    )

    print("\nSorted by marks")

    view_students()


# Total students
def total_students():

    print(
        f"\nTotal Students: {len(students)}"
    )


# Main program
while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Sort Alphabetically")
    print("7. Sort By Marks")
    print("8. Total Students")
    print("9. Exit")

    choice = input(
        "Enter your choice: "
    )

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
        sort_by_marks()

    elif choice == "8":
        total_students()

    elif choice == "9":
        print("Thank you!")
        break

    else:
        print("Invalid choice")  