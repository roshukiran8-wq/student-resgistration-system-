import csv
from validator import validate_contact
from analytics import analytics_report


def load_students():
    students = []

    try:
        with open("students_clean.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:
        print("Student file not found!")

    return students


def save_students(students):
    with open("students_clean.csv", "w", newline="") as file:
        fields = ["id", "name", "phone", "email"]

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)


def view_students(students):
    print("\nID\tName\tPhone\tEmail")

    for s in students:
        print(s["id"], s["name"], s["phone"], s["email"], sep="\t")


def search_student(students):
    search = input("Enter name, phone or email: ").lower()

    for s in students:
        if search in s["name"].lower() or search == s["phone"] or search == s["email"].lower():
            print(s)
            return

    print("Student not found!")


def register_student(students):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    valid, reason = validate_contact(name, phone, email)

    if not valid:
        print(reason)
        return

    for s in students:
        if s["phone"] == phone or s["email"].lower() == email.lower():
            print("Duplicate student!")
            return

    student = {
        "id": str(len(students) + 1),
        "name": name,
        "phone": phone,
        "email": email
    }

    students.append(student)
    save_students(students)

    print("Student registered successfully!")


def update_student(students):
    phone = input("Enter current phone number: ")

    for s in students:
        if s["phone"] == phone:

            name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            email = input("Enter new email: ")

            valid, reason = validate_contact(name, new_phone, email)

            if not valid:
                print(reason)
                return

            for other in students:
                if other != s and (
                    other["phone"] == new_phone or
                    other["email"].lower() == email.lower()
                ):
                    print("Duplicate details!")
                    return

            s["name"] = name
            s["phone"] = new_phone
            s["email"] = email

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student(students):
    value = input("Enter student ID or phone: ")

    for s in students:
        if s["id"] == value or s["phone"] == value:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")


def main():

    while True:
        students = load_students()

        print("\n===== STUDENT REGISTRATION SYSTEM =====")
        print("1. View All Students")
        print("2. Search Student")
        print("3. Register Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Analytics Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            register_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            analytics_report()

        elif choice == "7":
            save_students(students)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
