def count_words(string):
    mass_words = string.split(" ")
    clean_mass_words = []
    for word in mass_words:
        new_word = ''
        for char in word:
            if char.isalpha():
                new_word += char.lower()
        if new_word != '':
            clean_mass_words.append(new_word)
    # print(clean_mass_words)

    dict_word = {}
    for word in clean_mass_words:
        if word in dict_word:
            dict_word[word] += 1
        else:
            dict_word[word] = 1

    return dict_word


def main():
    string = "Doo bee doo bee doo"
    dict_word = count_words(string)
    print(dict_word)


if __name__ == '__main__':
    main()
