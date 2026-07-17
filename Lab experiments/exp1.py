
import re

text = """
Name: Rahul
Email: rahul@gmail.com
Phone: 9876543210
Website: https://www.example.com
"""

print("Original Text:")
print(text)

# Search for Email
email = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
if email:
    print("\nEmail Found:", email.group())

# Search for Phone Number
phone = re.search(r'\b\d{10}\b', text)
if phone:
    print("Phone Number Found:", phone.group())

# Find all words starting with 'R'
words = re.findall(r'\bR\w+', text)
print("Words starting with R:", words)

# Replace Rahul with Varun
new_text = re.sub("Rahul", "Varun", text)
print("\nAfter Replacement:")
print(new_text)