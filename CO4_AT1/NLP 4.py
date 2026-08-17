# Question 4: Syntax-Driven Semantic Analysis in Healthcare

sentences = [
    {
        "sentence": "Doctor prescribed medicine to patient.",
        "subject": "Doctor",
        "verb": "prescribed",
        "object": "medicine",
        "indirect": "patient"
    },
    {
        "sentence": "Patient reported severe headache.",
        "subject": "Patient",
        "verb": "reported",
        "object": "headache",
        "indirect": None
    },
    {
        "sentence": "Nurse monitored patient continuously.",
        "subject": "Nurse",
        "verb": "monitored",
        "object": "patient",
        "indirect": None
    },
    {
        "sentence": "Medicine reduced blood pressure.",
        "subject": "Medicine",
        "verb": "reduced",
        "object": "blood pressure",
        "indirect": None
    }
]

print("SYNTAX-DRIVEN SEMANTIC ANALYSIS")
print("-" * 70)

for item in sentences:

    print("\nSentence:", item["sentence"])
    print("Syntactic Structure: Subject - Verb - Object")

    print("Subject:", item["subject"])
    print("Verb:", item["verb"])
    print("Object:", item["object"])

    # Semantic role assignment
    if item["verb"] == "prescribed":
        print("Semantic Roles:")
        print("Doctor -> Agent")
        print("Medicine -> Theme")
        print("Patient -> Recipient")

    elif item["verb"] == "reported":
        print("Semantic Roles:")
        print("Patient -> Experiencer")
        print("Headache -> Symptom")

    elif item["verb"] == "monitored":
        print("Semantic Roles:")
        print("Nurse -> Agent")
        print("Patient -> Patient/Target")

    elif item["verb"] == "reduced":
        print("Semantic Roles:")
        print("Medicine -> Cause/Agent")
        print("Blood Pressure -> Theme")

print("\n" + "-" * 70)

print("\nROLE VALIDATION")

roles = {
    "Doctor": "Agent",
    "Medicine": "Theme/Cause",
    "Patient": "Recipient/Experiencer/Target",
    "Headache": "Symptom",
    "Nurse": "Agent",
    "Blood Pressure": "Theme"
}

for entity, role in roles.items():
    print(entity, "->", role)

print("\nPotential Parsing Errors:")
print("1. Incorrect subject identification can produce incorrect Agent roles.")
print("2. Incorrect object identification can change the Theme or Patient role.")
print("3. Prepositional phrase errors may confuse Recipient and Instrument roles.")
print("4. Medical terminology may cause incorrect semantic interpretation.")

print("\nRecommended Improvements:")
print("1. Use dependency parsing.")
print("2. Use medical NLP models.")
print("3. Use semantic role labeling.")
print("4. Use medical dictionaries and domain-specific ontologies.")
print("5. Validate results using clinical context.")
