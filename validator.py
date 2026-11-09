def validate_contact(name, phone, email):
    if not name.strip():
        return false, "Name is empty"
    if not phone.isdigit():
        return false, "Phone must contain only digits"
    if len(phone) != 10:
        return false, "Phone must be 10 digits"
    if phone[0] not in "6789":
        return false, "Invalid phone number"
    if email.count("@") != 1:
        return false, "Email must not contain spaces"
    local, domain = email.split("@")
    if not local:
        return false, "Email user is missing"
    if "." not in domain:
        return false, "Email domain must count a dot"
    if domain.strswith(".") or domain.endswith("."):
        return false, "Invalid email domain"
    return True,"valid contact"
