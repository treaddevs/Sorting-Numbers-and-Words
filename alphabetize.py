# Sam Treadwell
# 9/28/2022
# Fall 2022, CS 5001
# Sorting four words in alphabetical order

# Since the user is entering words the functions are strings
def main():
    print("This program sorts your words in alpabetical order")
    word1 = str(input("Enter a word: "))
    word2 = str(input("Enter a word: "))
    word3 = str(input("Enter a word: "))
    word4 = str(input("Enter a word: "))
# Next, we need to run each of the 24 scenarios for the ordering of the four words before printing
    if word1 <= word2 <= word3 <= word4:
        print(word1, word2, word3, word4)
    elif word1 <= word2 <= word4 <= word3:
        print(word1, word2, word3, word4)
    elif word1 <= word3 <= word2 <= word4:
        print(word1, word3, word2, word4)
    elif word1 <= word3 <= word4 <= word2:
        print(word1, word3, word4, word2)
    elif word1 <= word4 <= word2 <= word3:
        print(word1, word4, word2, word3)
    elif word1 <= word4 <= word3 <= word2:
        print(word1, word4, word3, word2)
    elif word2 <= word1 <= word3 <= word4:
        print(word2, word1, word3, word4)
    elif word2 <= word1 <= word4 <= word3:
        print(word2, word1, word4, word3)
    elif word2 <= word3 <= word1 <= word4:
        print(word2, word3, word1, word4)
    elif word2 <= word3 <= word4 <= word1:
        print(word2, word3, word4, word1)
    elif word2 <= word4 <= word1 <= word3:
        print(word2, word4, word1, word3)
    elif word2 <= word4 <= word3 <= word1:
        print(word2, word4, word3, word1)
    elif word3 <= word1 <= word2 <= word4:
        print(word3, word1, word2, word4)
    elif word3 <= word1 <= word4 <= word2:
        print(word3, word1, word4, word2)
    elif word3 <= word2 <= word1 <= word4:
        print(word3, word2, word1, word4)
    elif word3 <= word2 <= word4 <= word1:
        print(word3, word2, word4, word1)
    elif word3 <= word4 <= word1 <= word2:
        print(word3, word4, word1, word2)
    elif word3 <= word4 <= word2 <= word1:
        print(word3, word4, word2, word1)
    elif word4 <= word1 <= word2 <= word3:
        print(word4, word1, word2, word3)
    elif word4 <= word1 <= word3 <= word2:
        print(word4, word1, word3, word2)
    elif word4 <= word2 <= word1 <= word3:
        print(word4, word2, word1, word3)
    elif word4 <= word2 <= word3 <= word1:
        print(word4, word2, word3, word1)
    elif word4 <= word3 <= word1 <= word2:
        print(word4, word3, word1, word2)
    elif word4 <= word3 <= word2 <= word1:
        print(word4, word3, word2, word1)
main()








   