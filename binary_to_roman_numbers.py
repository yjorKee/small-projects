decimal_number = int(input('Enter a decimal number: '))
non_altered__decimal_number = decimal_number
roman_number = ''

numbers_with_letter_representation = [1000, 500, 100, 50, 10, 5, 1]
frequencies = [0, 0, 0, 0, 0, 0, 0]
frequency_index = 0

for number in numbers_with_letter_representation:
    number_of_leters = decimal_number // number
    decimal_number -= number * (number_of_leters)
    frequencies[frequency_index] = number_of_leters
    frequency_index += 1

roman_number += 'M'*frequencies[0] + 'D'*frequencies[1] + 'C'*frequencies[2] + 'L'*frequencies[3] + 'X'*frequencies[4] + 'V'*frequencies[5] + 'I'*frequencies[6]

roman_number = roman_number.replace('CCCC', 'CD')
roman_number = roman_number.replace('XXXX', 'XL')
roman_number = roman_number.replace('IIII', 'IV')
roman_number = roman_number.replace('VIV', 'IX')

print(f'{non_altered__decimal_number} in roman numbers is: {roman_number}')
