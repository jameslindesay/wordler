import pandas as pd
import random as rng
from colorama import Fore, Back, init
init()

def load_words():
    words_freqs = pd.read_csv('wordlists/valid_words_freqs.csv').sort_values('count', ascending=False)
    valid_words = words_freqs['word'].tolist()
    difficulty = 0 # maximum of 9
    goal_words  = valid_words[max(0, 200*(difficulty-2)):max(100,1000*difficulty)]
    return valid_words, goal_words

def print_wordle():
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
    print('\n                                                '+colours[3]+',,    '+colours[4]+',,')
    print(colours[0]+'`7MMF\'     A     `7MF\'                        '+colours[3]+'`7MM  '+colours[4]+'`7MM')
    print(colours[0]+'  `MA     ,MA     ,V                            '+colours[3]+'MM    '+colours[4]+'MM')
    print(colours[0]+'   VM:   ,VVM:   ,V    '+colours[1]+',pW"Wq.  '+colours[2]+'`7Mb,od8   '+colours[3]+',M""bMM    '+colours[4]+'MM   '+colours[5]+'.gP"Ya')
    print(colours[0]+'    MM.  M\' MM.  M\'   '+colours[1]+'6W\'   `Wb   '+colours[2]+'MM\' \"\' '+colours[3]+',AP    MM    '+colours[4]+'MM  '+colours[5]+',M\'   Yb')
    print(colours[0]+'    `MM A\'  `MM A\'    '+colours[1]+'8M     M8   '+colours[2]+'MM     '+colours[3]+'8MI    MM    '+colours[4]+'MM  '+colours[5]+'8M\"\"\"\"\"\"')
    print(colours[0]+'     :MM;    :MM;     '+colours[1]+'YA.   ,A9   '+colours[2]+'MM     '+colours[3]+'`Mb    MM    '+colours[4]+'MM  '+colours[5]+'YM.    ,')
    print(colours[0]+'      VF      VF       '+colours[1]+'`Ybmd9\'  '+colours[2]+'.JMML.    '+colours[3]+'`Wbmd\"MML.'+colours[4]+'.JMML. '+colours[5]+'`Mbmmd\' \n\n')

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

def main():
    print_wordle()
    valid_words, goal_words = load_words()
    target = rng.choice(goal_words)
    print(Fore.RESET + "Loaded " + str(len(valid_words)) + " valid words.")
    print("Loaded " + str(len(goal_words)) + " possible target words.\n")
    guesses = 0
    while guesses < 6:
        attempt = input("Enter guess: ")
        if word_valid(attempt, valid_words):
            if attempt == target:
                print(colour_attempt(attempt, target))
                guesses = 6
                print("\n\n")
            else:
                print(colour_attempt(attempt, target))
                guesses += 1
        else:
            print("Invalid word...")

if __name__=="__main__":
    main()
