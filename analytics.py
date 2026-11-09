from collections import Counter

def analyze_contacts(contacts):
    
    total =len(contacts)
    
    print("\n---- CONTACT ANALYTICS ----")
    print("Total valid contacts:",total)
    
    phone_prefixes = counter()
    email_domains = counter()

    for contact in contacts:

        phone = contact["phone"]
        email = contact["email"]

        phone_prefixes[phone[0]] += 1

        domain = email.split("@")[1]
        email_domains[domain] += 1

    print("\nPhone Prefix Counts:")

    for prefix, count in phone_prefixes.items():
        print(prefix, ":", count)

    print("\nEmail domain Count:")

    for doimain, count in email_domains.items():
        print(domain, ":", count)

    print("\n---- SUMMARY ----")
    print("Analytics completed successfully")
