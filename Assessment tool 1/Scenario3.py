import re

print("========== University Registration System ==========")

reg_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course_code = input("Enter Course Code: ")
semester = input("Enter Semester (1-8): ")
mobile = input("Enter Mobile Number: ")

status = True

# Register Number
if re.fullmatch(r"\d{2}[A-Z]{2}\d{4}", reg_no):
    print("Register Number: Valid")
else:
    print("Register Number: Invalid")
    status = False

# Email
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@university\.edu", email):
    print("Institutional Email: Valid")
else:
    print("Institutional Email: Invalid")
    status = False

# Course Code
if re.fullmatch(r"[A-Z]{2,3}\d{3}", course_code):
    print("Course Code: Valid")
else:
    print("Course Code: Invalid")
    status = False

# Semester
if re.fullmatch(r"[1-8]", semester):
    print("Semester: Valid")
else:
    print("Semester: Invalid")
    status = False

# Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")
    status = False

print("\n========== Registration Status ==========")

if status:
    print("Registration Successful")
else:
    print("Registration Failed")
    print("Please correct the invalid fields and try again.")