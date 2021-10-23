def combine_anagrams(words_array):
    anagrams = {}
    for word in words_array:
        if len(anagrams) == 0:
            anagrams[word] = [word]
        else:
            added = False
            for key in anagrams:
                if set(list(key)) == set(list(word)):
                    anagrams[key].append(word)
                    added = True
            if not added:
                anagrams[word] = [word]

    mas_anagrams = []
    for key in anagrams:
        mas_anagrams.append(anagrams[key])
    return mas_anagrams


def main():
    words_array = ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
    anagrams = combine_anagrams(words_array)
    print(anagrams)


if __name__ == '__main__':
    main()
