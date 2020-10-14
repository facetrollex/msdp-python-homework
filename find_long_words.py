def find_long_words(text, length):
    words = text.split()
    filteredWords = []
    for word in words:
        if (len(word) > length):
            filteredWords.append(word)
    return filteredWords

print(find_long_words("Python is an easy to learn, powerful programming language.", 1))
print(find_long_words("Python is an easy to learn, powerful programming language.", 5))