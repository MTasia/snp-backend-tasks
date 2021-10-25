def sort_list(mass):
    if len(mass) == 0:
        return []
    max_i = mass[0]
    min_i = mass[0]
    for i in range(len(mass)):
        max_i = max(max_i, mass[i])
        min_i = min(min_i, mass[i])

    new_mass = []
    for i in range(len(mass)):

        if mass[i] == min_i:
            new_mass.append(max_i)
        elif mass[i] == max_i:
            new_mass.append(min_i)
        else:
            new_mass.append(mass[i])
    new_mass.append(min_i)
    return new_mass


def main():
    mass = []
    new_mas = sort_list(mass)
    print(new_mas)


if __name__ == '__main__':
    main()
