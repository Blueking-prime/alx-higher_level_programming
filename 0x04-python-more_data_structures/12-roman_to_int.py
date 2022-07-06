#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    roman_string = str(roman_string)

    new_list = []
    roman_converts = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, \
                        'C' : 100, 'D' : 500, 'M' : 1000}
    for i in roman_string:
        new_list.append(i)
    k = 0

    for i in range(len(new_list)):
        for j in roman_converts:
            if new_list[i] is j:
                if new_list[i] == 'I' and i != len(new_list) - 1:
                    if new_list[i + 1] == 'X' or new_list[i + 1] == 'V':
                        new_list[i] = -1
                        k += 1
                        continue
                new_list[i] = roman_converts[j]
                k += 1

    if k != len(new_list):
        return 0

    return sum(new_list)
