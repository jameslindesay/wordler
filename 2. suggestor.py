import pandas as pd
import random as rng
import numpy as np
import itertools
import time
from tqdm import tqdm
from colorama import Fore, Back, init
init()

def timer_func(func):
    def wrapper_function(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args,  **kwargs)
        end = time.perf_counter()
        print(f"Time taken by {func.__name__} is {end-start}\n")
        return result
    return wrapper_function

def load_words():
    words_freqs = pd.read_csv('wordlists/valid_words_freqs.csv').sort_values('count', ascending=False)
    valid_words = words_freqs['word'].tolist()
    difficulty = 3 # maximum of 9
    goal_words  = rng.sample(valid_words[max(0, 200*(difficulty-2)):max(100,1000*difficulty)], 1000)
    return valid_words, goal_words

def print_wordler():
    colours = []
    i = 0
    while i < 6:
        seed_num = rng.randrange(0,3)
        if seed_num == 0:
            colour = Fore.RESET
        elif seed_num == 1:
            colour = Fore.YELLOW
        else:
            colour = Fore.GREEN
        colours.append(colour)
        i+=1
    colours.append(Fore.RED)
    print('\n                                                '+colours[3]+',,    '+colours[4]+',,')
    print(colours[0]+'`7MMF\'     A     `7MF\'                        '+colours[3]+'`7MM  '+colours[4]+'`7MM')
    print(colours[0]+'  `MA     ,MA     ,V                            '+colours[3]+'MM    '+colours[4]+'MM')
    print(colours[0]+'   VM:   ,VVM:   ,V    '+colours[1]+',pW"Wq.  '+colours[2]+'`7Mb,od8   '+colours[3]+',M""bMM    '+colours[4]+'MM   '+colours[5]+'.gP"Ya  '+colours[6]+'`7Mb,od8 ')
    print(colours[0]+'    MM.  M\' MM.  M\'   '+colours[1]+'6W\'   `Wb   '+colours[2]+'MM\' \"\' '+colours[3]+',AP    MM    '+colours[4]+'MM  '+colours[5]+',M\'   Yb   '+colours[6]+'MM\' \"\' ')
    print(colours[0]+'    `MM A\'  `MM A\'    '+colours[1]+'8M     M8   '+colours[2]+'MM     '+colours[3]+'8MI    MM    '+colours[4]+'MM  '+colours[5]+'8M\"\"\"\"\"\"   '+colours[6]+'MM     ')
    print(colours[0]+'     :MM;    :MM;     '+colours[1]+'YA.   ,A9   '+colours[2]+'MM     '+colours[3]+'`Mb    MM    '+colours[4]+'MM  '+colours[5]+'YM.    ,   '+colours[6]+'MM    ')
    print(colours[0]+'      VF      VF       '+colours[1]+'`Ybmd9\'  '+colours[2]+'.JMML.    '+colours[3]+'`Wbmd\"MML.'+colours[4]+'.JMML. '+colours[5]+'`Mbmmd\' '+colours[6]+'.JMML.\n\n')

def word_valid(word, valid_words):
    return word in valid_words

def colour_attempt(attempt, target):
    out_format = " "*20
    out_colours = []
    i = 0
    while i < len(attempt):
        char = attempt[i]
        if target[i] == char:
            out_format += Back.GREEN + Fore.BLACK + char
            out_colours.append(2)
        elif char in target:
            out_format += Back.YELLOW + Fore.BLACK + char
            out_colours.append(1)
        else:
            out_format += Back.WHITE + Fore.BLACK + char
            out_colours.append(0)
        i += 1
    return out_format + Back.RESET + Fore.RESET, out_colours

def word_is_possible(word_coloured, colours, word_to_check):
    i = 0
    while i < len(word_coloured):
        if colours[i] == 2:
            if word_to_check[i] != word_coloured[i]:
                return False
        elif colours[i] == 0:
            if word_coloured[i] in word_to_check:
                return False
        else:
            if word_coloured[i] not in word_to_check or word_to_check[i] == word_coloured[i]:
                return False
        i += 1
    return True

def possible_words_after(word_coloured, colours, list_possible_words_before):
    return [x for x in list_possible_words_before if word_is_possible(word_coloured, colours, x)]

def score_coloured_word_once(word_coloured, colours, list_possible_words_before):
    list_possible_words_after = possible_words_after(word_coloured, colours, list_possible_words_before)
    if len(list_possible_words_after) == 0: return 0
    probability = len(list_possible_words_after)/len(list_possible_words_before)
    information = probability * - (0 if probability == 0 else np.log2(probability))
    return information

def initialise_colour_combinations():
    choices = [0, 1, 2] # grey, yellow, green
    l = [choices] * 5
    return(list(itertools.product(*l)))

def fully_score_word(word, colour_combinations, list_possible_words_before):
    scores = [score_coloured_word_once(word, combination, list_possible_words_before) for combination in colour_combinations]
    return sum(scores)

@timer_func
def score_wordlist(colour_combinations, wordlist):
    scores = [fully_score_word(word, colour_combinations, wordlist) for word in tqdm(wordlist, desc="Scoring...")]
    return pd.DataFrame({'word':wordlist, 'score':scores})

def main():
    print_wordler()
    valid_words, goal_words = load_words()
    target = rng.choice(goal_words)
    print(Fore.RESET + "Loaded " + str(len(valid_words)) + " valid words.")
    print("Loaded " + str(len(goal_words)) + " possible target words.\n")
    colour_combinations = initialise_colour_combinations()
    list_possible_words_before = goal_words
    guesses = 0
    while guesses < 6:
        scored_words = score_wordlist(colour_combinations, list_possible_words_before)
        print(scored_words.sort_values('score', ascending=False).head(3))
        attempt = input("Enter guess: ")
        if word_valid(attempt, valid_words):
            out_format, out_colours = colour_attempt(attempt, target)
            print(out_format)
            if attempt == target:
                guesses = 6
                print("\n\n")
            else:
                guesses += 1
            list_possible_words_after = possible_words_after(attempt, out_colours, list_possible_words_before)
            list_possible_words_before = list_possible_words_after
        else:
            print("Invalid word...")

if __name__=="__main__":
    main()
