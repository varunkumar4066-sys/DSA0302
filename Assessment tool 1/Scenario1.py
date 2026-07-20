import re

# Sample Resume Data
resumes = [
"""
Name: John Smith
Email: johnsmith@gmail.com
Phone: +91-9876543210
Skills: Python, Java, SQL, Machine Learning
Experience: 3 years
""",
"""
Name: Priya Sharma
Email: priyasharma@yahoo.com
Phone: 9123456789
Skills: Java, SQL
Experience: 1 year
""",
"""
Name: David Wilson
Email: david.wilson@outlook.com
Phone: +91 9988776655
Skills: Python, NLP, Machine Learning
Experience: 5 years
""",
"""
Name: Sneha Reddy
Email: sneha.reddy@gmail.com
Phone: 9876501234
Skills: Python, SQL
Experience: 2 years
"""
]

technical_skills = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "NLP"
]

print("========== Resume Information Extraction ==========\n")

eligible_candidates = []

for resume in resumes:

    # Name
    name = re.search(r"Name:\s*(.*)", resume)
    name = name.group(1) if name else "Not Found"

    # Email
    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume
    )
    email = email.group() if email else "Not Found"

    # Phone
    phone = re.search(r"(\+91[- ]?)?\d{10}", resume)
    phone = phone.group() if phone else "Not Found"

    # Experience
    exp = re.search(r"(\d+)\s*year", resume, re.IGNORECASE)
    experience = int(exp.group(1)) if exp else 0

    # Skills
    found_skills = []

    for skill in technical_skills:
        if re.search(skill, resume, re.IGNORECASE):
            found_skills.append(skill)

    print("Candidate Summary")
    print("----------------------------")
    print("Name :", name)
    print("Email :", email)
    print("Phone :", phone)
    print("Experience :", experience, "Years")
    print("Skills :", ", ".join(found_skills))
    print()

    if experience >= 2 and "Python" in found_skills:
        eligible_candidates.append(name)

print("========== Eligible Candidates ==========")

if eligible_candidates:
    for candidate in eligible_candidates:
        print(candidate)
else:
    print("No eligible candidates found.")