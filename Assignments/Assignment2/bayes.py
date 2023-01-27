import kenlm
import nltk
import math

model = kenlm.LanguageModel('amb.binary')

while True:
    s = input('Enter a sentence to score: ')
    s = s.lower()
    score = model.score(s, bos = True, eos = True)
    l = len(list(model.full_scores(s)))
    perp = math.exp(-score / l)
    
    print("perp:", perp)
