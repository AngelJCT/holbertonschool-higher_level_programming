#!/usr/bin/python3
def roman_to_int(roman_string):
    #  dictionary with the value representation of roman letters to make the lookup faster
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0  #variable to store the integer value of the string

    #  if the string being passed is empty or not a string
    if roman_string is None or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        current_value = rom_val[roman_string[i]]  #  get the value of the current letter
        if i > 0:  #  if the current letter is not the first one
            prev_value = rom_val[roman_string[i - 1]]  #  get the value of the previous letter
            if current_value > prev_value:  #  if the current value is greater than the previous one
                result -= 2 * prev_value  #  subtract the previous value twice from the result variable to avoid adding it twice later on in the loop (once for the previous letter and once for the current letter)
        result += current_value  #  add the current value to the result variable
    return result
