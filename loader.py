import csv
import os
from validator import validate_contact

def load_contacts(filename="contacts.csv"):
    valid_contacts = []
    seen_phones = set()
    seen_emails = set()

    path = os.path.join(os.path.dirname(__file__),filename)
    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            phone = row["phone"]
            email = row["email"]

            is_valid, reason = validate_contact(name, phone, email)
            if is_valid:
                if phone not in seen_phones and email not in seen_emails:
                    valid_contacts.append(row)
                    seen_phones.add(phone)
                    seen_emails.add(email)
                else:
                    reason = "duplicate contacts"
            with open("ingection_log.txt","a")as log:
                log.write(name + " : " + reason + "\n")
                
    return valid_contacts

def save_clean_contacts(contacts):
    with open("students_clean.csv", "w" , newline="")as file:
        
        writer = csv.Dicwriter(
            file, fieldnames=["name", "phone", "email"]
        )
            
        writer.writeheader()
        writer.writerows(contacts)
        
