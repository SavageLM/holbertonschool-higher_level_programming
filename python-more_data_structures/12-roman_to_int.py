#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None:
        return int(0)
    if type(roman_string) != str:
        return int(0)
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
            'XC': 90, 'CD': 400, 'CM': 900}
    number = 0
    for i in range(len(roman_string)):
        if i > 0 and rome[roman_string[i]] > rome[roman_string[i - 1]]:
            number += rome[roman_string[i]] - 2 * rome[roman_string[i - 1]]
        else:
            number += rome[roman_string[i]]
    return int(number)
