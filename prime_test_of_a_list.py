
def prime_test_of_list_of_numbers(list_of_numbs):
    for number in list_of_numbs:

        range_of_numbers = range(2, int(number**0.5)+1)

        if number == 1:
            print('Primeness is not defined for 1')
        elif number == 2:
            print('2 IS prime')
        else:
            for possible_factor in range_of_numbers:
                if number % possible_factor == 0:
                    print(f'{number} is NOT prime')
                    break
            else:
                 print(f'{number} IS prime')


prime_test_of_list_of_numbers(range(2, 50))
