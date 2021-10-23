import re


def coincidence(string=None, borders=None):
    if string is None or borders is None:
        return []

    if len(string) == 0 or len(borders) == 0:
        return []

    ans = []
    start, end = borders[0], borders[-1]

    for elem in string:
        if elem is None:
            continue
        if str(elem).replace(".", "").isdigit():
            if start <= elem <= end:
                ans.append(elem)
    return ans


def main():
    string = [1, 2, 3, 4, 5]
    borders = range(3, 6)
    ans = coincidence(string, borders)
    print(ans)


if __name__ == '__main__':
    main()
