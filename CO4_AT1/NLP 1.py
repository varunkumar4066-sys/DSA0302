# Question 1: Semantic Representation in Customer Support Chatbots

queries = [
    ("Q1", "Activate Roaming", "ACTIVATE(Roaming, Customer)", "Activate Roaming"),
    ("Q2", "Deactivate Caller Tune", "DEACTIVATE(CallerTune, Customer)", "Activate Caller Tune"),
    ("Q3", "Query Data Balance", "QUERY(DataBalance, Customer)", "Query Data Balance"),
    ("Q4", "Activate 5G Service", "ACTIVATE(5GService, Customer)", "Activate 5G Service")
]

print("SEMANTIC REPRESENTATION ANALYSIS")
print("-" * 60)

correct = 0

for qid, actual, representation, predicted in queries:
    action = representation.split("(")[0]
    obj = representation.split("(")[1].split(",")[0]

    print("\nQuery ID:", qid)
    print("Semantic Representation:", representation)
    print("Action:", action)
    print("Object:", obj)
    print("Actual Intent:", actual)
    print("Predicted Intent:", predicted)

    if actual == predicted:
        print("Status: Correct")
        correct += 1
    else:
        print("Status: ERROR")

accuracy = (correct / len(queries)) * 100

print("\n" + "-" * 60)
print("Correct Predictions:", correct)
print("Total Queries:", len(queries))
print("Chatbot Accuracy:", accuracy, "%")

print("\nConclusion:")
print("Q2 contains a semantic interpretation error.")
print("The actual intent is to DEACTIVATE Caller Tune,")
print("but the chatbot predicted ACTIVATE Caller Tune.")