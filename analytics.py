import csv

def analytics_report():

    students = []

    with open("students_clean.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    total = 20
    accepted = len(students)
    rejected = total - accepted

    if total > 0:
        accuracy = (accepted / total) * 100
    else:
        accuracy = 0

    print("\n===== STUDENT ANALYTICS REPORT =====")

    print("Total Contacts:", total)
    print("Accepted Contacts:", accepted)
    print("Rejected Contacts:", rejected)
    print("Acceptance Rate:", accuracy, "%")

    prefix_count = {"9": 0, "8": 0, "7": 0, "6": 0}
    domain_count = {}

    for student in students:

        phone = student["phone"]
        email = student["email"]

        prefix = phone[0]

        if prefix in prefix_count:
            prefix_count[prefix] += 1

        domain = email.split("@")[1]

        domain_count[domain] = domain_count.get(domain, 0) + 1

    print("\nPhone Prefix Distribution:")

    for prefix, count in prefix_count.items():
        print(prefix + "-series:", count)

    print("\nEmail Domain Breakdown:")

    for domain, count in domain_count.items():
        print(domain, ":", count)


if __name__ == "__main__":
    analytics_report()
