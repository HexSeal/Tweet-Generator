import random
import sys

def rearrange(words):
    rearrange_words = []
    while len(words) > 0:
        # get a random word
        random_word = random.choice(words)
        # if it's not already in the list
        if not random_word in rearrange_words:
            # append it to rearragne words and remove it from words so that it can't be reused
            rearrange_words.append(random_word)
            del words[words.index(random_word)]
    return rearrange_words

if __name__ == "__main__":
    # makes sure there's some arguments
    if len(sys.argv) >= 2:    
        words = sys.argv[1:]
        new_words = rearrange(words)
        print(' '.join(new_words))
    else:
        print("Need more words")
        letters = rearrange(list('Failure'))
        print(''.join(letters))
