import histogram
import sys
import random

# Helped by https://github.com/sprajjwal  

# Helper function for getting the count number of objects in the histogram
def word_sampler(histogram):
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

def test_sampler(hist):
    """ tests sampler by running it 10000 times, uncomment line 32 for this"""
    test_words = []
    for _ in range(10000):
        test_words.append(word_sampler(hist))
    test_hist = histogram.histogram_dictionary(test_words)
    for item in test_hist.keys():
        print(f"{item}: {test_hist[item]}")

if __name__ == "__main__":
    # file = sys.argv[1:]
    f = open('hpb1_hist.txt')
    words = f.read().split("\n")
    hist = histogram.histogram_dictionary(words)
    final_word = word_sampler(hist)
    print(final_word)
    # test_sampler(hist)

    
    #print(word_sampler(hist))