#!/usr/bin/env python3

def get_letters(word):
    i = 0
    letters = []
    while i < len(word):
        letters.append(word[i])
        i += 1
    return letters

nameLetters = get_letters("Breno")

print(nameLetters)
