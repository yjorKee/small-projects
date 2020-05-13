

def prime_test(list_of_numbers):
    list_of_primes = []
    list_of_composites = []
    
    for number in list_of_numbers:
        list_of_possible_factors = list(range(2, int((number**0.5)+1)))
        factors = []
        for each_number in list_of_possible_factors:
            if number % each_number == 0:
                factors.append(each_number)
        if len(factors) == 0:
            list_of_primes.append(number)
        else:
            list_of_composites.append(number)

    print(f'Primes between 2 and {limit}: {list_of_primes}')
    # print(f'Composites between 2 and {limit}: {list_of_composites}')


limit = 10
prime_test(list(range(2, limit)))


