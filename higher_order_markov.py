from dictogram import Dictogram
from histogram import open_file, run
import random

class SecondOrderChain(dict):
    def __init__(self, word_list=None, order = 1):
        # Initialize the super class
        super(SecondOrderChain, self).__init__()
        self.types = 0
        self.tokens = 1
        self.order = order

        # If there's words, start a chain
        if word_list:
            self.word_walk(word_list, order)

    def word_walk(self, words, order):
        for i in range(len(words) - order):
            # If the tuple is not in keys then create a new word tuple and add to the counters
            if tuple(words[i: i + order]) not in self.keys():
                self[tuple(words[i: i+order])] = []
                self.types += 1
            self[tuple(words[i: i + order])].append(tuple(words[i+1: i+order+1]))
            self.tokens += 1
        for key in self.keys():
            self[key] = Dictogram(self[key])

    def get_text(self, path = 'harry_potterb1.txt'):
        text = open_file(path)
        return text 

    # Got from @github.com/sprajjwal, very nice sampling and text formatting
    def sample(self, key):
        """gets a random word  that appears after key"""
        return self[key].sample()

    def get_string(self, length=1):
    # Returns a string of len based on markov's chain
        start = random.choice(list(self.keys()))
        string = list(start)
        prev = start
        for _ in range(length - self.order):
            prev = self.sample(prev)
            string.append(f"{prev[self.order-1]}")
        string = ' '.join(string)
        if string[len(string)-1] != '.':
            string += "."
        return string.capitalize()

if __name__ == "__main__":
    word_doc = "harry_potterb1.txt"
    file = run(word_doc)
    word_walk(file, 1)