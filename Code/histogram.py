
# histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
filename = ""

def histogram(source_text):
    with open("source_text", "r") as f:
        histogram = source_text.split()
        return histogram

def unique_words(histogram):
    unique_words = []
    for word in histogram:
        if word not in unique_words:
            unique_words.append(word)
        else:
            continue
        return unique_words

def frequency(word, histogram):
    for _ in histogram:
        if _ == word:
            frequncy += 1
        return frequency

def log_words(histogram):
    different_words = unique_words(histogram)
    for word in different_words:
        word_frequency = frequency(word, histogram)
        print(word + "\t" + word_frequency)

# Attempt at optimization, trying to search by first letter so the code doesn't have to analyze every word
    # for _ in histogram:
    #     word.split()
    #     if word[0] == _[0]:
    #         if _ == word:
    #             frequency += 1
    #     else: 
    #         continue