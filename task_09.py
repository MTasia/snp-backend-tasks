def connect_dicts(dict1, dict2):
    # Search priorities dict
    sum1 = 0
    for key in dict1:
        sum1 += dict1[key]
    sum2 = 0
    for key in dict2:
        sum2 += dict2[key]

    # Connect dict
    new_dict = {}
    if sum1 > sum2:
        for key in dict1:
            if dict1[key] >= 10:
                new_dict[key] = dict1[key]
        for key in dict2:
            if key not in new_dict and dict2[key] >= 10:
                new_dict[key] = dict2[key]
    else:
        for key in dict2:
            if dict2[key] >= 10:
                new_dict[key] = dict2[key]
        for key in dict1:
            if key not in new_dict and dict1[key] >= 10:
                new_dict[key] = dict1[key]

    # Sort new dict
    sort_dict = {}
    while len(new_dict) > 0:
        min_num = 1000000
        key_min_num = 0
        for key in new_dict:
            if min_num > new_dict[key]:
                min_num = new_dict[key]
                key_min_num = key
        sort_dict[key_min_num] = min_num
        new_dict.pop(key_min_num)

    return sort_dict


def main():
    dict1, dict2 = {"a": 14, "b": 12}, {"c": 11, "a": 15}
    sort_dict = connect_dicts(dict1, dict2)
    print(sort_dict)


if __name__ == '__main__':
    main()
