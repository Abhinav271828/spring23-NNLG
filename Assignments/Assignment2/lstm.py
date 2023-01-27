#https://github.com/hjc18/language_modeling_lstm/blob/master/main.py

from model import *
from corpus import *
from torch import tensor
from math import exp

mdl = torch.load('model_test.pt')
mdl.eval()

dct = torch.load('dict.pt')
w2i = dct.word2idx

while True:
    s = input('Enter a sentence to score: ')
    s = s.split() + ['<eos>']
    l = len(s)
    inp = tensor([w2i[w] if w in w2i else w2i['<unk>'] for w in s]).unsqueeze(1)
    hid = mdl.init_hidden(1)
    
    logits, _ = mdl(inp, hid)
    perp = exp(torch.nn.functional.cross_entropy(logits, inp.squeeze(1).data) / float(l+1))
    print("perp:", perp)
