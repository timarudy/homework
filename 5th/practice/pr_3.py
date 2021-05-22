import sys
f = open('/Users/maccheese/Desktop/5th/file.txt', 'r')
text_str = f.read().split()

frequency = {}

def word_amount(word):
    word.lower()
    count = frequency.get(word,0)
    frequency[word] = count + 1

list(map(word_amount, text_str))

frequency_list = frequency.keys()
 

for words in frequency_list:
    print(words, frequency[words])
