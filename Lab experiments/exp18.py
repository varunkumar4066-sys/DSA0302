import re

expression = "Likes(John, Apple)"

pattern = r"([A-Za-z]+)\(([^,]+),\s*([^)]+)\)"

result = re.match(pattern, expression)

print("Expression:", expression)

if result:
    predicate = result.group(1)
    arg1 = result.group(2)
    arg2 = result.group(3)

    print("Predicate:", predicate)
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)
    print("Expression is valid.")
else:
    print("Expression is invalid.")