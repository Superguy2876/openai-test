import string

# Function to remove punctuation from words
def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

# Read text2 into a set of lines
with open('output.txt', 'r', encoding='utf-8') as file:
    text2_set = set(file.read().lower().split('\n'))

# Read text1 and check each word against the set
with open('text1.txt', 'r', encoding='utf-8') as file:
    text1_words = file.read().lower().split()

# Check if each word from text1 exists in the set of text2
for word in text1_words:
    # Remove punctuation from the word
    clean_word = remove_punctuation(word)
    if clean_word not in text2_set:
        print(clean_word)