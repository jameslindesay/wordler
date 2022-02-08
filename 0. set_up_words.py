import pandas as pd

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
session = WolframLanguageSession("C:/Program Files/Wolfram Research/Wolfram Engine/13.0/WolframKernel.exe")

valid_words = []
with open("valid_words.txt", "r") as f:
  for word in f:
    valid_words.append(word.strip())

df = pd.DataFrame({'word':valid_words})

print(df)

df2 = pd.read_csv('unigram_freq.csv')
print(df2['word'])

df3 = df2[df2['word'].str.len() == 5]

df3.to_csv('valid_words_freqs.csv', index=False)
