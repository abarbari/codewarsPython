import sys


#
# ROMAN NUMBERAL ENCODER
#
#   https://www.codewars.com/kata/51b62bf6a9c58071c600001b
# 
# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#

def solution(n):
    roman_num_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    roman_str = ""
    if n <= 0:
        return None
    for key in roman_num_dict.keys():
        while n >= key:
            roman_str = roman_str + roman_num_dict[key]
            n = n - key
    return roman_str

for item in sys.argv[1::]:
    try:
        temp = solution(int(item))
        if temp:
            print(f'Converted Numeric value "{item}" into Roman Numeral {temp}')
        else:  
            print(f'Argument "{item}" contains values that are not within limits of the function.')
    except Exception:
        print(f'Argument "{item}" contains values that are non numerical or not within limits of the function.')
    
    

