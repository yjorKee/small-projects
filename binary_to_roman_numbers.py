binary_number = int(input('Enter a binary number: '))
non_altered__binary_number = binary_number
roman_number = ''

numbers_with_letter_representation = [1000, 500, 100, 50, 10]
frequencies = [0, 0, 0, 0, 0]
frequency_index = 4

for number in numbers_with_letter_representation:
    number_of_leters = binary_number // number
    binary_number -= number * (number_of_leters)
    frequencies[frequency_index] = number_of_leters
    frequency_index -= 1

roman_number += 'M'*frequencies[4] + 'D'*frequencies[3] + 'C'*frequencies[2] + 'L'*frequencies[1] + 'X'*frequencies[0]

if (binary_number == 1) or (binary_number == 2) or (binary_number == 3):
    roman_number += 'I'*binary_number
elif binary_number == 4:
    roman_number += 'IV'
elif binary_number == 5:
    roman_number += 'V'
elif binary_number == 6:
    roman_number += 'VI'
elif binary_number == 7:
    roman_number += 'VII'
elif binary_number == 8:
    roman_number += 'VIII'
elif binary_number == 9:
    roman_number += 'IX'

print(f'{non_altered__binary_number} in roman numbers is: {roman_number}')
