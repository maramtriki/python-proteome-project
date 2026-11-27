def read_words(filename):
    words = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().upper()
            if len(word) >= 3:
                words.append(word)

    return words

words = read_words("english-common-words.txt")
print("Nombre de mots sélectionnés :", len(words))
print(words[:10])


def read_sequences(filename):
    proteome = {}
    protein_id = ""
    sequence = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(">"):
                if protein_id:
                    proteome[protein_id] = sequence
                protein_id = line.split("|")[1]
                sequence = ""
            else:
                sequence += line.strip()

        if protein_id:
            proteome[protein_id] = sequence
    return proteome

proteome = read_sequences("human-proteome.fasta")
print("Nombre de protéines :", len(proteome))
print("Séquence de O95139 :", proteome["O95139"])


def search_words_in_proteome(words, proteome):
    results = {}

    for word in words:
        count = 0
        for sequence in proteome.values():
            if word in sequence:
                count += 1
        results[word] = count
        if count > 0 :
        print(word, "found in", count, "sequences")
    return results

words = read_words("english-common-words.txt")
proteome = read_sequences("human-proteome.fasta")
results = search_words_in_proteome(words, proteome) 


def find_most_frequent_word(results, proteome):
    max_word = ""
    max_count = 0

    for word, count in results.items():
        if count > max_count:
            max_count = count
            max_word = word
            
    percentage = (max_count / len(proteome)) * 100
    print(max_word, "found in", max_count, "sequences")
    print(" The most frequent word is ", max_word )
    print("Percentage:", round(percentage, 2), "%")

    return max_word, max_count, percentage

words = read_words("english-common-words.txt")
proteome = read_sequences("human-proteome.fasta")
results = search_words_in_proteome(words, proteome)
find_most_frequent_word(results, proteome)

def search_word_occurrences(words, proteome):
    results = {}

    for word in words:
        count = 0
        for sequence in proteome.values():
            count += sequence.count(word)
        results[word] = count
    return results






 

