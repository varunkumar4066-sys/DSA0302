import re

products = [
    "Python Programming Book",
    "Java Programming Book",
    "SQL Database Guide",
    "Machine Learning Basics",
    "NLP with Python",
    "Python Cookbook",
    "Wireless Mouse",
    "Bluetooth Keyboard",
    "Gaming Laptop",
    "Laptop Stand",
    "USB Keyboard",
    "Python Data Science",
    "Java Developer Guide",
    "Smart Watch",
    "Phone Charger"
]

def search_products(pattern, description, flags=0):

    print("\n" + "=" * 50)
    print(description)
    print("=" * 50)

    matches = []

    for product in products:
        if re.search(pattern, product, flags):
            matches.append(product)

    if matches:
        print("Matching Products:")
        for item in matches:
            print("-", item)
    else:
        print("No matching products found.")

    print("Total Matches:", len(matches))


# Exact Search
keyword = input("Enter exact keyword: ")

search_products(
    r"\b" + re.escape(keyword) + r"\b",
    "Exact Keyword Search"
)

# Prefix Search
prefix = input("\nEnter prefix: ")

search_products(
    r"^" + re.escape(prefix),
    "Prefix Search"
)

# Suffix Search
suffix = input("\nEnter suffix: ")

search_products(
    re.escape(suffix) + r"$",
    "Suffix Search"
)

# Partial Search
partial = input("\nEnter partial keyword: ")

search_products(
    re.escape(partial),
    "Partial Keyword Search"
)

# Case-Insensitive Search
text = input("\nEnter keyword for case-insensitive search: ")

search_products(
    re.escape(text),
    "Case-Insensitive Search",
    re.IGNORECASE
)