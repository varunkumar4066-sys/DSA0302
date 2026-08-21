import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple was founded by Steve Jobs in California."

doc = nlp(text)

print("Text:")
print(text)

print("\nNamed Entities:")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)