#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = 0
	roman_numerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
            }
    for a in reversed(roman_string):
        roman_figs = roman_numerals[a]
        num += roman_figs if num < roman_figs * 5 else -roman_figs
    return num
