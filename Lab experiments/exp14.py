singular_subjects = ["boy", "girl", "student"]
plural_subjects = ["boys", "girls", "students"]

singular_verbs = ["plays", "runs", "reads"]
plural_verbs = ["play", "run", "read"]

sentence = "The boy plays cricket"

words = sentence.lower().split()

subject = words[1]
verb = words[2]

print("Sentence:", sentence)

if subject in singular_subjects and verb in singular_verbs:
    print("Agreement: Correct")
elif subject in plural_subjects and verb in plural_verbs:
    print("Agreement: Correct")
else:
    print("Agreement: Incorrect")