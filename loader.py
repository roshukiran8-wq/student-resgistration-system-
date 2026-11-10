import csv
import os
from validator import validate_contact

def load_contacts():

    students = []
    seen_phones = set()
    seen_emails = set()
    rejected = {}

    file_path = os.path.join(os.path.dirname(__file__),"contacts.csv")

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        total = 0

        for row in reader:
            total += 1

            name = row["name"]
            phone = row["phone"]
            email = row["email"]

            valid, reason = validate_contact(name, phone, email)

            if not valid:
                rejected[reason] = rejected.get(reason, 0) + 1
                continue

            if phone in seen_phones:
                rejected["Duplicate phone"] = rejected.get("Duplicate phone", 0) + 1
                continue

            if email in seen_emails:
                rejected["Duplicate email"] = rejected.get("Duplicate email", 0) + 1
                continue

            seen_phones.add(phone)
            seen_emails.add(email)

            student = {
                "id": len(students) + 1,
                "name": name,
                "phone": phone,
                "email": email
            }

            students.append(student)

    output_path = os.path.join(os.path.dirname(__file__),"students_clean.csv")

    with open(output_path, "w", newline="") as file:
        fields = ["id", "name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(students)

    print("STUDENT DATA REPORT")
    print("-------------------")
    print("Total records:", total)
    print("Accepted records:", len(students))
    print("Rejected records:", total - len(students))

    print("\nRejection Reasons:")

    for reason, count in rejected.items():
        print(reason, ":", count)


if __name__ == "__main__":
    load_contacts()
