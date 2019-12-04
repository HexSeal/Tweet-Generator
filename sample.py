from histogram import histogram_dictionary
import sys
import random

# Helped by https://github.com/sprajjwal  

# Helper function for getting the count number of objects in the histogram
def sample(histogram):
    """Takes a histogram and returns a word based of its frequency"""
    count = 0
    count += sum(histogram.values())
    sum_prob = 0
    lucky_number = random.random()
    for key in histogram.keys():
        prob = histogram[key]/count
        if lucky_number > sum_prob and lucky_number <= sum_prob + prob:
            return key
        sum_prob += prob

def sentence_creator(histogram, num_words):
    """ tests sampler by running it 10000 times, uncomment line 36 for this"""
    words = []
    sentence = []
    for _ in range(0, num_words):
        words.append(sample(histogram))
    hist = histogram_dictionary(words)
    for item in hist.keys():
        sentence.append(item)
    sentence_str = " ".join(sentence)
    return sentence_str #sentence


def test_sampler(histogram):
    """ tests sampler by running it 10000 times, uncomment line 36 for this"""
    test_words = []
    for _ in range(10000):
        test_words.append(sample(histogram))
    test_hist = histogram_dictionary(test_words)
    for item in test_hist.keys():
        print(f"{item}: {test_hist[item]}")

if __name__ == "__main__":
    # file = sys.argv[:1]
    # num_words = sys.argv[:1]
    num_words = 8

    f = open('harry_potterb1.txt')
    words = f.read().split()
    hist = histogram_dictionary(words)
    print(sentence_creator(hist, num_words))

# Tests
    # print(test_sampler(hist, num_words))
    # print(word_sampler(hist))