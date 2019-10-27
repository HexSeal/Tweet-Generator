import sys
import random

def dictionary_word(word_list, word_num):
    random_words = []
    for _ in range(word_num):
        random_words.append(random.choice(word_list))
    return random_words

if __name__ == "__main__":
    words_num = sys.argv[1]
    words_num = int(words_num)

    with open("/usr/share/dict/words", "r") as f:
        word_list = f.read().splitlines()
        random_words = dictionary_word(word_list, words_num)
        print(" ".join(random_words))
