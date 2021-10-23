def sort_list(mass):
    if len(mass) == 0:
        return 0
    max_i = mass[0]
    index_max_i = 0
    min_i = mass[0]
    index_min_i = 0
    for i in range(len(mass)):
        if max_i < mass[i]:
            max_i = mass[i]
            index_max_i = i
        if mass[i] < min_i:
            min_i = mass[i]
            index_min_i = i
    mass[index_min_i], mass[index_max_i] = max_i, min_i
    mass.append(min_i)


def main():
    mass = []
    sort_list(mass)
    print(mass)


if __name__ == '__main__':
    main()
