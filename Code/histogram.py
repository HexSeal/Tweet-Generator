from pprint import pprint
import sys
import random

# histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}

# Helped by github.com/ysawiris
def stripWordPunctuation(word):
    return word.strip("&.,()<>\"}{'~?!;*:[]-+/&—\n ")

def open_file(source_text):
    
    #open and read file 
    f = open(source_text, 'r')
    lines = f.read().split()
    #split each word to be seperate 
    
    for line in lines:
        line = stripWordPunctuation(line)

    f.close()

    #print(lines)
    #print(line)

    return lines

def histogram_dictionary(source_text):
    #define our histogram 
    histogram = {}

    #loop though our file_text and add text to our histogram 
    for text in source_text:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    print(histogram)
    return histogram

def unique_words(histogram):
    unique_words = []
    for word in histogram:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words

def frequency(word, histogram):
    frequency = 0
    for _ in histogram:
        if _ == word:
            frequency += 1
    return frequency


# Attempt at optimization, trying to search by first letter so the code doesn't have to analyze every word
    # for _ in histogram:
    #     word.split()
    #     if word[0] == _[0]:
    #         if _ == word:
    #             frequency += 1
    #     else: 
    #         continue

if __name__ == "__main__":
    source_text = 'harry_potterb1.txt'
    histogram = histogram_dictionary(source_text)
    text = open_file(source_text)
    histogram_dictionary(text)


    # Extra functions for different data structures, helped by github.com/anikamorris


# def file_or_string(source_text):
#     file_data = ''
#     if '.txt' in source_text:
#         file = open(source_text, 'r')
#         file_data = file.read()
#         file.close()
#     else:
#         file_data = source_text
#     return file_data

# def list_of_lists_histogram(source_text):
#     words = []
#     file_data = file_or_string(source_text)
#     words = file_data.split()
#     histogram = []
#     for word in words:
#         is_in_histogram = False
#         for i in range(len(histogram)):
#             if word == histogram[i][0]:
#                 histogram[i][1] += 1
#                 is_in_histogram = True

#         if is_in_histogram == False:
#             histogram.append([word, 1])
    
#     return histogram

# def list_of_tuples_histogram(source_text):
#     words = []
#     file_data = file_or_string(source_text)
#     words = file_data.split()
#     histogram = []
#     for word in words:
#         is_in_histogram = False
#         for i in range(len(histogram)):
#             if word == histogram[i][0]:
#                 histogram[i] = (word, (histogram[i][1])+1)
#                 is_in_histogram = True

#         if is_in_histogram == False:
#             histogram.append((word, 1))
    
#     return histogram
