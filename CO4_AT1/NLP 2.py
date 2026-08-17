# Question 2: First-Order Predicate Calculus for Smart Manufacturing

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

produces = {
    "M1": "Gear",
    "M2": "Bolt",
    "M3": "Gear",
    "M4": "Shaft"
}

print("FIRST-ORDER PREDICATE CALCULUS")
print("-" * 60)

# Represent production data using predicates
print("\nProduction Data:")

for machine, status in machines.items():
    if status == "Active":
        print("Active(" + machine + ")")
    else:
        print("Maintenance(" + machine + ")")

print("\nProduction Relationships:")

for machine, product in produces.items():
    print("Produces(" + machine + ", " + product + ")")

# Apply rules
print("\nPredicate Inference:")
available_products = set()
affected_products = set()

for machine, product in produces.items():

    if machines[machine] == "Active":
        print("Active(" + machine + ") -> Producing(" + machine + ")")
        print("Produces(" + machine + "," + product + ") AND Active(" +
              machine + ") -> Available(" + product + ")")
        available_products.add(product)

    elif machines[machine] == "Maintenance":
        print("Maintenance(" + machine + ") -> NOT Producing(" + machine + ")")
        affected_products.add(product)

print("\nCurrently Available Products:")
for product in sorted(available_products):
    print(product)

print("\nProducts Affected by Maintenance:")
for product in sorted(affected_products):
    print(product)

print("\nConclusion:")

if "Gear" in affected_products:
    print("Gear production is affected because M3 is under maintenance.")
else:
    print("Gear production is not affected.")