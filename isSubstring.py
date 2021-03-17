#!/usr/bin/env python3

def isSubstring(s1,s2):
    i = 0
    j = 0
    counter = 0
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            for counter in range(len(s1)):
                if s1[i] != s2[j]:
                    return False
                else:
                    i = i + 1
                    j = j + 1
                    counter = counter + 1
            return True
        else:
            j = j+1
    return False

answer = isSubstring('oot', 'barfootex')
print(answer)
