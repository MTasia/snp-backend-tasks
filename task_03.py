def max_odd(mass):
    if len(mass) == 0:
        return None
    max_elem = 0
    for elem in mass:
        if elem is None:
            continue
        if elem is list:
            for i in elem:
                if str(i).replace(".", "").isdigit():
                    if i % 2 == 1:
                        max_elem = max(max_elem, i)
            continue
        if str(elem).replace(".", "").isdigit():
            if elem % 2 == 1:
                max_elem = max(max_elem, elem)
    if max_elem == 0:
        return None
    return max_elem


def main():
    mass = ['ololo', None]
    max_elem = max_odd(mass)
    print(max_elem)


if __name__ == '__main__':
    main()
