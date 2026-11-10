def validate_contact(name, phone, email):
    
    
    if len(name.strip()) == 0:
        return False, "Name cannot be empty"

    if len(phone) != 10 or not phone.isdigit():
        return False, "Phone must contain 10 digits"

    if phone[0] not in "6789":
        return False, "Phone must start with 6, 7, 8 or 9"

    if email.count("@") != 1:
        return False, "Invalid email"

    if " " in email:
        return False, "Email cannot contain spaces"

    parts = email.split("@")

    if len(parts[0]) == 0:
        return False, "Email username is missing"

    domain = parts[1]

    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False, "Invalid email domain"

    return True, "Valid contact"
