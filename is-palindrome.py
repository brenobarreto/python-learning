#!/usr/bin/env python3

def isPalindrome(s):

    first = 0
    second = -1

    for i in range(len(s)//2):
        if s[first] != s[second]:
            return False
        else:
            first = first + 1
            second = second - 1

    return True

answer = input("Enter the sentence: ")

if isPalindrome(answer):
    print('This is a palindrome')
else:
    print('This is NOT a palindrome')
