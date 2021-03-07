def reverseLetters(word):
    i = -1
    while i >= -len(word):
        print(word[i], end="")
        i-=1
    print("\n")