from transformers import pipeline

# Load the English-to-French translation model
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

# Get input from the user
text = input("Enter English text: ")

# Translate the text
result = translator(text)

# Display the translation
print("English :", text)
print("French  :", result[0]["translation_text"])