import nltk

with open('The Ambassadors.txt', 'r') as f:
    for line in f:
        for sentence in nltk.sent_tokenize(line):
            print(' '.join(nltk.word_tokenize(sentence)).lower())
