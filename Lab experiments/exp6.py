text = "I love learning natural language processing"

words = text.split()

bigrams = []

for i in range(len(words) - 1):
    bigrams.append((words[i], words[i + 1]))

print("Text:")
print(text)

print("\nBigrams:")
for pair in bigrams:
    print(pair)

generated_text = ""

for pair in bigrams:
    generated_text += pair[0] + " "

generated_text += bigrams[-1][1]

print("\nGenerated Text:")
print(generated_text)