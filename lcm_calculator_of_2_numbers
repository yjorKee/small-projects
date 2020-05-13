# Code to calculate the LCM of any 2 numbers


def lcm_hcf_calculator(number1, number2):
    # Define 2 different lists of multiples of 2 numbers 
    multiples_of_number1 = list(range(number1, (number1*number2)+1, number1))
    multiples_of_number2 = list(range(number2, (number2*number1)+1, number2))
    lcm_candidates = []
    
    # Add any common multiples to the third list
    for n in multiples_of_number1 and multiples_of_number2:
        if n in multiples_of_number1:
            if n in multiples_of_number2:
                lcm_candidates.append(n)
                
    # After sorting the common list the first element will be the LCM
    lcm_candidates.sort()
    lcm = lcm_candidates[0]
    
    print(f'LCM of {number1} and {number2} is {lcm}')
    print(f'HCF is {int(number1*number2/lcm)}')


lcm_hcf_calculator(69, 420)


