import pandas as pd
import random as rng
import curses
from colorama import Fore, Back, init
init()

def load_words():
    words_freqs = pd.read_csv('valid_words_freqs.csv')
    valid_words = words_freqs['word'].tolist()
    difficulty = 3
    goal_words  = valid_words[0:1000*difficulty]
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

def input_attempt(message):
    try:
        stdscr = curses.initscr()
        stdscr.clear()
        stdscr.addstr(message)
        attempt = stdscr.getstr(1, 0, 5)
    except:
        raise
    finally:
        curses.endwin() # restore the terminal to its original operating mode.
    return attempt

def colour_attempt(attempt, target):
    out = "                   "
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
    print("I have {0} apples and {1} pears".format(input(), input()))
    valid_words, goal_words = load_words()
    target = rng.choice(goal_words)
    print(Fore.RESET + "Loaded " + str(len(valid_words)) + " valid words.")
    print("Loaded " + str(len(goal_words)) + " goal words.\n")
    guesses = 0
    stdscr = curses.initscr()
    while guesses < 6:
        attempt = input_attempt("enter guess: ")
        if word_valid(attempt, valid_words):
            if attempt == target:
                print(colour_attempt(attempt, target))
                guesses = 6
            else:
                print(colour_attempt(attempt, target))
                guesses += 1
        else:
            print("Invalid word...")

if __name__=="__main__":
    main()
