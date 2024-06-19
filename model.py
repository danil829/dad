from random import choice
import gensim
from gensim.models import KeyedVectors
from pymystem3 import Mystem

model = KeyedVectors.load_word2vec_format('custom_embedding.txt',binary=False)

def get_lemma(word):
    m = Mystem()
    lemma = m.lemmatize(word)
    return lemma[0]

def select_random_word():
    item = choice(list(model.key_to_index_items())[:100])
    return item[0].split('_')[0]

def get_most_simmilar_dict(word,topn):
    d = {k.split('_')[0]:k for k in model.key_to_index}
    vals = model.most_similar(d[word],topn=topn)
    d_ = {k.split('_')[0]: i + 2 for i,(k,v)in enumerate(vals)if ':'not in  k}
    return d_

def get_placement(word,word_dict):
    lemma = get_lemma(word)
    if lemma in word_dict:
        return word_dict[lemma]
    return -1

def init():
    init_word = select_random_word()
    word_dict = get_most_simmilar_dict(init_word, 100000)
    return init_word, word_dict
if __name__ == '__main__':
    init_word, word_dict = init()
    print('Initial word:',word_dict)
    print('Word dictionary:',word_dict)
    input('Press Enter to exit...')