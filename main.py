from validator import validate_contact
from loader import load_contacts, save_clean_contacts
from analytics import analyze_contacts

def view_contacts(contacts):

    print("\n--- STUDENTS CONTACTS ---")

    if not contacts:
        print("no contacts found.")
        return
    for conatct in contacts:
        print(contact["name"], contact["phone"], contact["email"])

def search_cintact(contacts):

    search = input("Enter namr or phone to search:").lower()

    found = false

    for contact in contacts:
        if (search in contact["name"].lower() or search in contact["phone"]):
            print(contact)
            found = true
        if not found:
            print("contact not found.")

def register_student(contacts):
    name = input("Enter name:")
    phone = input("Enter phone:")
    email = input("Enter email:")

    valid, reason =  validate_contact(name, phone, email)

    if not valid:
        print(reason)
        return

    for contact in contacts:
        if contact["phone"] == phone or contact["email"] == email:
            print("Duplicate contact.")
            return

    contacts.append({"name" : name, "phone" : phone, "email" : email})

    save_clean_contacts(contacts)
    print("Student registered successfully.")

def update_student(contacts):
    phone = input("enter phone number to update:")

    for contact in contacts:
        if contact["phone"] == phone:
            name = input("enter new name:")
            new_phone = input("enter new phone:")
            email = input("enter new email:")

            valid, reason = validate_contact(name, new_phone, email)

            if not valid:
                print(reason)
                return

            contact["name"]=name
            contact["phone"]=new_phone
            contact["email"]=email

            save_clean_contacts(contacts)
            print("contacts updated successfully.")
            return
        print("contact not found.")

def delete_student(contacts):
    phone = input("Enter phone number to delete:")
    for contact in contacts:
        if contact["phone"]== phone:

            contacts.remove(contact)
            save_clean_contacts(contacts)

            print("contacts deleted successfully.")
            return
        print("contacts not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n==== STUDENT REGISTRATION STYSTEM ====")
        print("1. view Contacts")
        print("2. Search contact")
        print("3. Register student")
        print("4. Update student")
        print("5. Delete student")
        print("6. analytics")
        print("7. exit")

        choice = input("Enter your choice:")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            register_student(contacts)
        elif choice == "4":
            update_student(contacts)
        elif choice == "5":
            delete_student(contacts)
        elif choice == "6":
            analyze_contacts(contacts)
        elif choice == "7":
            print("Thank you for using the system!")

            break
        else:
            print("invalid choice. Try again.")

if __name__ == "__main__":
    main()
            
        
