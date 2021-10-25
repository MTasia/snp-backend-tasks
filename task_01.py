def is_palindrome(string):
    string = str(string)
    string_alpha = []
    for char in string:
        if char.isalpha() or char.isnumeric():
            string_alpha.append(char.lower())

    n = len(string_alpha)

    if n < 1:
        return False

    for i in range((n + 1) // 2):
        if string_alpha[i] != string_alpha[(n - 1) - i]:
            return False

    return True


def main():
    string = "Madam, I'm Adam!"
    ans = is_palindrome(string)
    print(ans)


if __name__ == '__main__':
    main()
