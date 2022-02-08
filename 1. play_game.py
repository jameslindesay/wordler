import pandas as pd
import random as rng
from colorama import Fore, Back, init
init()

words_freqs = pd.read_csv('wordlists/valid_words_freqs.csv')
valid_words = words_freqs['word'].tolist()
difficulty = 3
goal_words  = valid_words[0:1000*difficulty]

def print_wordle():
    colours = []
    i = 0
    while i < 6:
        seed_num = rng.randrange(0,4)
        if seed_num == 0:
            colour = Fore.YELLOW
        elif seed_num == 1:
            colour = Fore.GREEN
        else:
            colour = Fore.RESET
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

def is_word_valid(word):
    return word in valid_words

def main():
    print_wordle()
    print(Fore.RESET + "Loaded " + str(len(valid_words)) + " valid words.")
    print("Loaded " + str(len(goal_words)) + " goal words.")
    # x = input("Enter test word: ")
    # print(is_word_valid(x))

if __name__=="__main__":
    main()
