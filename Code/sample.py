import histogram
import sys
import random

# Helper function for getting the total number of objects in the histogram

def get_total(histogram):
    word_count = 0
    for word in histogram:
        word_count += 1
    return word_count

# Take the token(total number of objects) and divide the frequency of the words by tokens to get a decimal. Then use that to select a random word based on frequency.
def sample_by_frequency(histogram):
    # Get the "weight" of every letter together
    token = get_total(histogram)
    # Get the lucky index
    random_index = random.randint(1, token)

    # Iterate through all the words 
    for word in histogram:
        # Subtract the words value from the histogram
        random_index = random_index - word.values
        if random_index <= 0:
            return word

if __name__ == "__main__":
    source_text = 'harry_potterb1.txt'
    text = histogram.open_file(source_text)
    histogram_text = histogram.histogram_dictionary(text)
    sample_by_frequency(histogram_text)