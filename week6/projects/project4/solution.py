# Project 4 — Word Counter
# Author: Davud Azizi

sentence = input("Enter a sentence: ")

for char in ",.!?":
    sentence = sentence.replace(char, "")

words = sentence.lower().split()

total_words = len(words)
total_characters = len(sentence.replace(" ", ""))

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_characters}")
print("Word frequency:")

for word, count in frequency.items():
    print(f"  {word} -> {count}")
