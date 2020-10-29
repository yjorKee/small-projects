'''
LCM(num1, num2, num3) = LCM(LCM(num1, num2), num3)
Generalising this, we can write a program for finding the LCM of
any number of numbers
'''


def LCM(num1, num2):

    possible_lcms = []

    mults_of_num1 = range(num1, num1*num2+1, num1)
    mults_of_num2 = range(num2, num2*num1+1, num2)

    for multiple1 in mults_of_num1:
        for multiple2 in mults_of_num2:
            if multiple1 == multiple2:
                possible_lcms.append(multiple1)

    return possible_lcms[0]

list_of_numbers = range(1, 11) # enter list of numbers here
lcm = 1

for num in list(list_of_numbers):
    lcm = LCM(num, lcm)

print(lcm)
