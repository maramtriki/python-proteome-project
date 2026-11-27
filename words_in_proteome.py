
# Question 1

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



# Question 2

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


# Question 3

def search_words_in_proteome(words, proteome):
    results = {}

    for word in words:
        count = 0
        for sequence in proteome.values():
            if word in sequence:
                count += 1
        results[word] = count
        if count > 0:
            print(word, "found in", count, "sequences")

    return results



# Question 4

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



# Question 5

def search_word_occurrences(words, proteome):
    results = {}

    for word in words:
        count = 0
        for sequence in proteome.values():
            count += sequence.count(word)
        results[word] = count
    return results

def find_most_frequent_occurrence(results):

    max_word = ""
    max_count = 0

    for word, count in results.items():

        if count > max_count:
            max_count = count
            max_word = word

    print("Pour la question 5 :")
    print("The most frequent word in the human proteome is:", max_word)
    print("Number of occurrences:", max_count)

    return max_word, max_count


# Programme principal

words = read_words("english-common-words.txt")
proteome = read_sequences("human-proteome.fasta")

# Question 3
results = search_words_in_proteome(words, proteome)

# Question 4
find_most_frequent_word(results, proteome)

# Question 5
occurrences = search_word_occurrences(words, proteome)
find_most_frequent_occurrence(occurrences)





 

