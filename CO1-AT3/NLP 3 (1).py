import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

print("Text:")
print(text)

while True:

    print("\nMenu")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Quit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("Dates:", re.findall(r"\d{2}/\d{2}/\d{4}", text))

    elif choice == 2:
        print("Phone Numbers:", re.findall(r"\b\d{10}\b", text))

    elif choice == 3:
        print("Hashtags:", re.findall(r"#\w+", text))

    elif choice == 4:
        print("Mentions:", re.findall(r"@\w+", text))

    elif choice == 5:
        prefix = input("Enter prefix: ")
        print("Matching Words:", re.findall(r"\b" + prefix + r"\w*", text))

    elif choice == 6:
        suffix = input("Enter suffix: ")
        print("Matching Words:", re.findall(r"\w*" + suffix + r"\b", text))

    elif choice == 7:
        word = input("Enter word: ")
        if re.search(r"\b" + word + r"\b", text):
            print("Word Found")
        else:
            print("Word Not Found")

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")
