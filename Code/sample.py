import histogram
import sys
import random


# Take the token(total number of objects) and divide the frequency of the words by tokens to get a decimal. Then use that to select a random word based on frequency.

def sample_by_frequency(histogram):
    token = sum(histogram.values)

    random_index = random.randint()

    for word in histogram:
        if word == histogram[random_index]:
            return word

def word_percentage(histogram, word):
    histo_len = len(histogram)
    word_freq = histogram.frequency(word, histogram)
    word_percentage = (word_freq/histo_len) * 100
    return word_percentage

if __name__ == "__main__":