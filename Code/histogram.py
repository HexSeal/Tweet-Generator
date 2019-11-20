from pprint import pprint
import sys
import random
import re

# histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}

def open_file(file):
    with open(file, "r") as f:
        words = f.read().split()
    words = [re.sub('[^A-Za-z]+', '', word).lower() for word in words]

    return words

def histogram_dictionary(source_text):
    #define our histogram 
    histogram = {}

    #loop though our file_text and add text to our histogram 
    for text in source_text:
        if text in histogram.keys():
            histogram[text] += 1
        else:
            histogram[text] = 1
    # print(histogram)
    return histogram

def unique_word(hist):
    """ counts number of unique words in a histogram"""
    return len(hist.keys())

def frequency(word, hist):
    """ gives the frequency of word in the histogram"""
    if word.lower() in hist.keys():
        return hist[word.lower()]
    else:
        return 0

def read_hist(f):
    """Reads a histogram type file into a dictionary """
    lines = f.readlines()
    histogram = {}
    for line in lines:
        line = line.split()
        histogram[line[0]] = line[1]
    return histogram

def write_hist(file_name, histogram):
    """ writes a histogram to a file"""
    with open(file_name, "w+") as f:
        for key in histogram.keys():
            f.write(f"{key} {hist[key]}\n")

# Attempt at optimization, trying to search by first letter so the code doesn't have to analyze every word
    # for _ in histogram:
    #     word.split()
    #     if word[0] == _[0]:
    #         if _ == word:
    #             frequency += 1
    #     else: 
    #         continue

if __name__ == "__main__":
    open_file("harry_potterb1.txt")
    with open("harry_potterb1.txt", 'r') as f:
        
        words = f.read().split()
        hist = histogram_dictionary(words)
        freq = list(hist)
    write_hist("hpb1_hist.txt", hist)


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
