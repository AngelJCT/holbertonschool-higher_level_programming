#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        current_value = rom_val[roman_string[i]]
        if i > 0:
            prev_value = rom_val[roman_string[i - 1]]
            if current_value > prev_value:
                result -= 2 * prev_value
        result += current_value
    return result
