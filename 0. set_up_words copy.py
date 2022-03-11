import pandas as pd

valid_words = []
with open("wordlists/valid_words.txt", "r") as f:
  for word in f:
    valid_words.append(word.strip())

valid_words = pd.DataFrame({'word':valid_words})

print(valid_words)

unigram_word_freqs = pd.read_csv('wordlists/unigram_freq.csv')
print(unigram_word_freqs['word'])

five_letter_word_freqs = unigram_word_freqs[unigram_word_freqs['word'].str.len() == 5]

valid_five_letter_word_freqs = pd.merge(valid_words, five_letter_word_freqs, on = 'word', how = 'inner')

print(valid_five_letter_word_freqs)

valid_five_letter_word_freqs.to_csv('wordlists/valid_words_freqs.csv', index=False)

