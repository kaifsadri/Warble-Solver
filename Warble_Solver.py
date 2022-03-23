#!/usr/bin/env python


def match(m, g):
    main = list(m)
    guess = list(g)
    result = ["R"] * len(main)
    if len(m) != len(g):
        return result
    for pos in range(len(main)):
        if main[pos] == guess[pos]:
            result[pos] = "G"
            main[pos] = "*"
            guess[pos] = "*"
    for pos in range(len(main)):
        if guess[pos] != "*" and guess[pos] in main:
            result[pos] = "Y"
            main.remove(guess[pos])
    return "".join(result)


lexicon = set(line.strip() for line in open("words.txt").readlines() if len(line) == 7)
num_guesses = 0
while True:
    num_guesses += 1
    if (not lexicon) or num_guesses > 6:
        print("\n!!!!! I LOST !!!!!")
        break
    guess = lexicon.pop()
    wr = input(f"\nI guess {guess.upper()}. What does Warble say? ").strip().upper()
    while len(wr) != 6 or any(c not in "GYR" for c in wr):
        wr = input(f"\nInvalid input!!! I guess {guess.upper()}. What does Warble say? ").strip().upper()
    if wr == "G" * len(guess):
        print("\n!!!!! I WON !!!!!")
        break
    lexicon = set(word for word in lexicon if match(word, guess) == wr)
