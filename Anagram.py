#!/usr/bin/env python


def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


def file_to_list():
    d = []

    with open("words_alpha.txt") as f:
        for line in f:
            d.append(line.strip())

    return d


def main():
    word_list = file_to_list()

    user_input = input('Enter a word to check for anagrams: ')

    for word in word_list:
        if user_input != word and is_anagram(user_input, word):
            print(word)


if __name__ == '__main__':
    main()
