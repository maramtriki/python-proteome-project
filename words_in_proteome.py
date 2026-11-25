def read_words(filename):
    words = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            word = line.upper()
            if len(word) >= 3:
                words.append(word)

    return words

words = read_words("english-common-words.txt")

print("Nombre de mots sélectionnés :", len(words))
print(words[:10])