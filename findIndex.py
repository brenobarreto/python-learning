def find(word, letter, initialIndex):
    index = initialIndex
    while index < len(word):
        if word[index] == letter:
            return index
        index+= 1
    return -1