
# Frequency Counter Using Dictionaries
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
