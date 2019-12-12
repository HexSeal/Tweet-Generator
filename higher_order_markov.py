from dictogram import Dictogram
from histogram import open_file, run
import random
import sys

class SecondOrderChain(dict):
    def __init__(self, word_list=None, order = 2):
        # Initialize the super class
        super(SecondOrderChain, self).__init__()
        self.types = 0
        self.tokens = 1
        self.order = order

        # If there's words, start a chain
        if word_list:
            self.link_chain(word_list, 3)
            # self['start'] = Dictogram([''])
            # self['end'] = Dictogram([''])

    def link_chain(self, words, order):
        for i in range(len(words) - order):
            # If the tuple is not in keys then create a new word tuple and add to the counters
            if tuple(words[i: i + order]) not in self.keys():
                self[tuple(words[i: i+order])] = []
                self.types += 1
            self[tuple(words[i: i + order])].append(tuple(words[i+1: i+order+1]))
            self.tokens += 1
        for key in self.keys():
            self[key] = Dictogram(self[key])

    def get_text(self, path = 'jordanpeterson.txt'):
        # Reuses open_file from histogram, grabs text
        
        text = open_file(path)
        return text 

    def sample(self, key):
        """gets a random word  that appears after key"""
        return self[key].sample()

    def word_walk(self, len=1):
        # Start at a designated start word, create the list on that
        start = random.choice(list(self.keys()))
        prev = random.choice(list(self.keys()))
        # Can't use string because it's Python syntax
        strin = list(start)
        for _ in range(len - self.order - 1):
            prev = self.sample(prev)
            strin.append(f"{prev[self.order-1]}")
        strin = ' '.join(strin)
        strin += "."
        return strin.capitalize()

if __name__ == "__main__":
    word_list = SecondOrderChain.get_text("jordanpeterson.txt")
    markov_chain = SecondOrderChain(word_list)

    print(markov_chain.word_walk(8))