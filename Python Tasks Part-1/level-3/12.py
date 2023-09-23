def email_slicer(email):
    try:
        username, domain = email.split('@')
        return (username, domain)
    except:
        return "Invalid email format"


email = "ragab5434@gmail.com"

print(email_slicer(email))