import json
import os

FILE_NAME = "students.json"


def load_students():
    """Load student records from a file."""
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = json.load(file)

        if isinstance(students, dict):
            return students

        print("Warning: Invalid student data. Starting with an empty list.")
        return {}

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student records.")
        return {}


def save_students(students):
    """Save student records to a file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True

    except OSError:
        print("Error: Could not save student records.")
        return False


def register_student(students):
    print("\n========== REGISTER STUDENT ==========")

    admission_number = input("Enter admission number: ").strip().upper()

    if not admission_number:
        print("Error: Admission number cannot be empty.")
        return

    if admission_number in students:
        print("Error: This admission number is already registered.")
        return

    full_name = input("Enter student's full name: ").strip()

    if not full_name:
        print("Error: Student name cannot be empty.")
        return

    course = input("Enter course name: ").strip()

    if not course:
        print("Error: Course name cannot be empty.")
        return

    while True:
        year_input = input("Enter year of study (1-6): ").strip()

        try:
            year = int(year_input)

            if 1 <= year <= 6:
                break

            print("Please enter a year between 1 and 6.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    phone = input("Enter phone number: ").strip()

    if not phone:
        print("Error: Phone number cannot be empty.")
        return

    student = {
        "admission_number": admission_number,
        "full_name": full_name,
        "course": course,
        "year": year,
        "phone": phone
    }

    students[admission_number] = student

    if save_students(students):
        print("\nStudent registered successfully!")
        print("Admission Number:", admission_number)
        print("Name:", full_name)
        print("Course:", course)
        print("Year of Study:", year)
        print("Phone:", phone)
    else:
        students.pop(admission_number, None)
        print("Registration was not completed because saving failed.")


def view_students(students):
    print("\n========== REGISTERED STUDENTS ==========")

    if not students:
        print("No students registered yet.")
        return

    for number, student in students.items():
        print("-" * 40)
        print("Admission Number:", number)
        print("Full Name:", student["full_name"])
        print("Course:", student["course"])
        print("Year of Study:", student["year"])
        print("Phone:", student["phone"])

    print("-" * 40)
    print("Total students:", len(students))


def search_student(students):
    print("\n========== SEARCH STUDENT ==========")

    admission_number = input(
        "Enter admission number to search: "
    ).strip().upper()

    student = students.get(admission_number)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent found!")
    print("Admission Number:", student["admission_number"])
    print("Full Name:", student["full_name"])
    print("Course:", student["course"])
    print("Year of Study:", student["year"])
    print("Phone:", student["phone"])


def update_student(students):
    print("\n========== UPDATE STUDENT ==========")

    admission_number = input(
        "Enter admission number to update: "
    ).strip().upper()

    student = students.get(admission_number)

    if student is None:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")

    new_name = input(
        f"Full name [{student['full_name']}]: "
    ).strip()

    new_course = input(
        f"Course [{student['course']}]: "
    ).strip()

    new_year = input(
        f"Year of study [{student['year']}]: "
    ).strip()

    new_phone = input(
        f"Phone [{student['phone']}]: "
    ).strip()

    if new_name:
        student["full_name"] = new_name

    if new_course:
        student["course"] = new_course

    if new_year:
        try:
            year = int(new_year)

            if not 1 <= year <= 6:
                print("Invalid year. Keeping the existing year.")
            else:
                student["year"] = year

        except ValueError:
            print("Invalid year. Keeping the existing year.")

    if new_phone:
        student["phone"] = new_phone

    if save_students(students):
        print("Student details updated successfully!")


def delete_student(students):
    print("\n========== DELETE STUDENT ==========")

    admission_number = input(
        "Enter admission number to delete: "
    ).strip().upper()

    student = students.get(admission_number)

    if student is None:
        print("Student not found.")
        return

    print("Student:", student["full_name"])
    print("Admission Number:", admission_number)

    confirmation = input(
        "Are you sure you want to delete this student? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("Deletion cancelled.")
        return

    deleted_student = students.pop(admission_number)

    if save_students(students):
        print("Student deleted successfully!")
    else:
        students[admission_number] = deleted_student
        print("Deletion was cancelled because saving failed.")


def main():
    students = load_students()

    while True:
        print("\n")
        print("=" * 45)
        print(" UNIVERSITY STUDENT REGISTRATION SYSTEM")
        print("=" * 45)
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Count Students")
        print("7. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            register_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("\nTotal registered students:", len(students))

        elif choice == "7":
            print("\nThank you for using the system!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()