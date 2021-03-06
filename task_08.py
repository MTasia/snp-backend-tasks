def multiply_numbers(string=None):
    string = str(string)

    multiply = 1
    have_num = False
    for elem in string:
        if elem.isdigit():
            multiply *= int(elem)
            have_num = True

    if not have_num:
        return None

    return multiply


def main():
    mass = [1, 2, 3]
    ans = multiply_numbers(mass)
    print(ans)


if __name__ == '__main__':
    main()
