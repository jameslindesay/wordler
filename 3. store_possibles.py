import pandas as pd
from tqdm import tqdm
from joblib import Parallel, delayed
import itertools
import pickle

def load_words():
  words_freqs = pd.read_csv('wordlists/valid_words_freqs.csv').sort_values('count', ascending=False)
  valid_words = words_freqs['word'].tolist()
  return valid_words

def word_is_possible(uin, colours, word_to_check):
    i = 0
    while i < len(uin):
        if colours[i] == '2':
            if word_to_check[i] != uin[i]:
                return False
        elif colours[i] == '0':
            if uin[i] in word_to_check:
                return False
        else:
            if uin[i] not in word_to_check or word_to_check[i] == uin[i]:
                return False
        i += 1
    return True

def initialise_colour_combinations():
    choices = [0, 1, 2] # grey, yellow, green
    l = [choices] * 5
    combinations = list(itertools.product(*l))
    return([''.join(map(str, x)) for x in combinations])

def add_word_to_dict(word, dict, colourings, valid_words):
  dict[word] = {}
  for colouring in colourings:
      possibles = [x for x in valid_words if word_is_possible(word, colouring, x)]
      if len(possibles) != 0:
        dict[word][colouring] = possibles
  return dict


def possibilities_dict(colourings, valid_words):
  dict = {}
  dict = Parallel(n_jobs = -1, backend = 'multiprocessing', verbose = 1)\
    (delayed(add_word_to_dict)(word, dict, colourings, valid_words[0:100]) for word in valid_words)
  return dict

def main():
  valid_words = load_words()
  colourings = initialise_colour_combinations()
  dict = possibilities_dict(colourings, valid_words)

  print(dict['about'])

  f = open("wordlists/possibles.pkl","wb")
  pickle.dump(dict,f)
  f.close()


if __name__=="__main__":
    main()