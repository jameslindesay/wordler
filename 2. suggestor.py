import pandas as pd
import random as rng
import math
import itertools
from colorama import Fore, Back, init
init()

def load_words():
    words_freqs = pd.read_csv('wordlists/valid_words_freqs.csv').sort_values('count', ascending=False)
    valid_words = words_freqs['word'].tolist()
    difficulty = 0 # maximum of 9
    goal_words  = valid_words[max(0, 200*(difficulty-2)):max(100,1000*difficulty)]
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
    out = " "*20
    i = 0
    while i < 5:
        char = attempt[i]
        if target[i] == char:
            out += Back.GREEN + Fore.BLACK + char
        elif char in target:
            out += Back.YELLOW + Fore.BLACK + char
        else:
            out += Back.WHITE + Fore.BLACK + char
        i += 1
    return out + Back.RESET + Fore.RESET

def word_is_possible(word_coloured, colours, word_to_check):
    validity = []
    i = 0
    while i < 5:
        if colours[i] == 0: # grey
            validity.append(word_coloured[i] not in word_to_check)
        elif colours[i] == 1: # yellow
            validity.append(word_to_check[i] != word_coloured[i] and word_coloured[i] in word_to_check)
        else: # green
            validity.append(word_to_check[i] == word_coloured[i])
        i += 1
    return all(validity)

def possible_words_after(word_coloured, colours, possible_words_before):
    return [x for x in possible_words_before if word_is_possible(word_coloured, colours, x)]

def score_coloured_word_once(word_coloured, colours, list_possible_words_before):
    list_possible_words_after = possible_words_after(word_coloured, colours, list_possible_words_before)
    probability = len(list_possible_words_after)/len(list_possible_words_before)
    information = probability * - math.log2(probability)
    return information

def initialise_colour_combinations():
    choices = [0, 1, 2] # grey, yellow, green
    l = [choices] * 5
    return(list(itertools.product(*l)))

def fully_score_word(word, colour_combinations, list_possible_words_before):
    # TODO: 
    x = map(score_coloured_word_once, word, colour_combinations, list_possible_words_before)
    print(sum(x))

def main():
    print_wordler()
    valid_words, goal_words = load_words()
    target = rng.choice(goal_words)
    print(Fore.RESET + "Loaded " + str(len(valid_words)) + " valid words.")
    print("Loaded " + str(len(goal_words)) + " possible target words.\n")
    print(word_is_possible("point", [0,0,1,2,0], "xixnx"))
    print(possible_words_after("point", [2,0,0,0,0], goal_words))
    print(score_coloured_word_once("point", [2,0,0,0,0], goal_words))
    colour_combinations = initialise_colour_combinations()
    fully_score_word("doggy", colour_combinations, goal_words)
    # guesses = 0
    # while guesses < 6:
    #     attempt = input("Enter guess: ")
    #     if word_valid(attempt, valid_words):
    #         if attempt == target:
    #             print(colour_attempt(attempt, target))
    #             guesses = 6
    #             print("\n\n")
    #         elif guesses == 5:
    #             print(target)
    #         else:
    #             print(colour_attempt(attempt, target))
    #             guesses += 1
    #     else:
    #         print("Invalid word...")

if __name__=="__main__":
    main()
